import os
from openai import OpenAI

from utils import match_content_in_quote, match_content_list_in_quote

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL"),
)

query_list = [
    "Build chat pdf bot",
    "Build ai search bot",
    "An app that asks OpenAI to generate a dinner list",
    "Help me import CSV into Airtable.",
    "Help me import CSV into Obsidian.",
    "Help me import CSV into Notion.",
    "Explain what happened in the video I uploaded.",
    "Explain what happened in the audio I uploaded.",
    "Explain what happened in the image I uploaded.",
    "build app user can input some text, then use ai to generate images based on the input. "
    "build app user can input some text, then use ai to generate speech based on the input. "
]
code_assistant_id = 'asst_4VuT8MH3frdp33CSAF8fMYpd'
rewrite_assistant_id = 'asst_plL8kwVdowSOk4sYXE5KP5bw'

path = 'output/version_4'

def get_tech_solution(client : OpenAI, query: str, rewrite_assistant_id: str):
    prompt = """You are an expert in technology, specializing in prompt fine-tuning and technical solution design. Your responsibility is to rewrite the user's request into a more detailed technical solution. First, provide a simple description enclosed within `<tech>` and `</tech>` tags. Then, ensure that each step of the solution is enclosed within `<step>` and `</step>` tags to facilitate prompt splitting."""
    prompt += f"""Here is the user's request:
                   <user-query>
                   {query}
                   </user-query>
                """

    thread = client.beta.threads.create()
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=rewrite_assistant_id,
    )
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        response_text = messages.data[0].content[0].text.value
    else:
        print(run.status)

    return response_text

def split_tech_solution(solution: str):
    # split the solution into steps and tech description
    tech = match_content_in_quote(solution, "<tech>", "</tech>")
    steps = match_content_list_in_quote(solution, "<step>", "</step>")
    return tech, steps

for i, query in enumerate(query_list):
    os.makedirs(f'{path}/{i}', exist_ok=True)

    tech_solution = get_tech_solution(client, query, rewrite_assistant_id)

    print(f'Tech solution: \n{tech_solution}\n')

    base_prompt = """You are an expert on writing Streamlit apps.
        Find resolutions from your knowledge base, and generate the Python code based on the user's request.
        Only show the Python code, no other content should be shown.
        Some requirements you should consider:
        1. The generated code must be a fully functional Streamlit app.
        2. If the user asks for data visualization, you can only use Streamlit default charts and Altair charts (recommended) or Matplotlib charts.
        3. If datasets are provided, use them as the user wants.
        4. Do not add features that the user does not ask for.
        5. Always trust the example in the tags <example-query> and <example-code>; they are real workable examples using some latest Streamlit features.
        6. If databases are provided, use them as the user wants, using SQLAlchemy as the database engine, such as `engine = create_engine(os.getenv("DATABASE_URL"))`.
        \n
        """

    tech, steps = split_tech_solution(tech_solution)
    print(f'Tech: \n{tech}\n')
    print(f'Steps: \n{steps}\n')

    new_code_prompt = base_prompt + f"""Here is the user's request:
                  <user-query>
                  {tech}
                  </user-query>
                  \n
                  """
    new_thread = client.beta.threads.create()
    client.beta.threads.messages.create(
        thread_id=new_thread.id,
        role="user",
        content=new_code_prompt
    )

    client.beta.threads.messages.create(
        thread_id=new_thread.id,
        role="user",
        content="\n Here is the technical solution, which can be used as a reference: \n"
    )

    for step in steps:
        new_message = client.beta.threads.messages.create(
            thread_id=new_thread.id,
            role="user",
            content=f"\n{step}\n"
        )

    client.beta.threads.messages.create(
        thread_id=new_thread.id,
        role="user",
        content="\n Generate the workable Streamlit app code wrapped in a code block suitable for a Streamlit app.\n",
    )

    new_run = client.beta.threads.runs.create_and_poll(
        thread_id=new_thread.id,
        assistant_id=code_assistant_id,
        instructions="Please generate a workable Streamlit app code that can be run directly based on the user demand."
    )
    if new_run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=new_thread.id
        )
        response_text = messages.data[0].content[0].text.value
    else:
        print(new_run.status)

    print(f'token {i} done, {new_run.usage.prompt_tokens}, {new_run.usage.completion_tokens}, {new_run.usage.total_tokens}')
    response_text = match_content_in_quote(response_text, "```python", "```")

    with open(f'{path}/{i}/main.py', 'w', encoding='utf-8') as file:
        file.writelines(response_text)
