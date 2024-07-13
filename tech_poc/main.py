
import os
from openai import OpenAI

from utils import match_content_in_quote
from tech import get_tech_solution

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE_URL"),
)


query_list = [
    "Build chat pdf bot",
    "Build ai search bot",
    "An app that ask open ai to generate a dinner list",
    "Help me import CSV into Airtable.",
    "Help me import CSV into Obsidian.",
    "Help me import CSV into Notion.",
]
code_assistant_id = 'asst_4VuT8MH3frdp33CSAF8fMYpd'
rewrite_assistant_id = 'asst_lhMmzVVNx5uJVFXomQUFmrnq'



for i, query in enumerate(query_list):


    os.makedirs(f'output/{i}', exist_ok=True)

    tech_solution = get_tech_solution(client, query, rewrite_assistant_id)

    print(f'Tech solution: \n{tech_solution}\n')

    base_prompt = """You are an expert on writing streamlit app.
        Find resolutions from you knowledge base, and generate the python code based on user's request.
        Only show the python code, no other content should be shown.
        Some requirements you should consider:
        1. If the user ask for data visualization, you can only use streamlit default charts and altair charts (recommended) or matplotlib charts.
        2. If datasets is provided, use it as the user want.
        3. Do not add feature that user does not ask for.
        4. You should always trust the example in tag <example-query> and <example-code>, they are real workable example which use some latest streamlit features.
        5. If databases is provided, use it as the user want, using sqlachemy as database engine, such as `engine = create_engine(os.getenv("DATABASE_URL"))`.
        \n
        """

    origin_prompt = base_prompt + f"""Here is the user's request:
                  <user-query>
                  {query}
                  </user-query>
                  Generate the python code wrapped in python code block.
                  \n
                  """

    print(f'Origin prompt: \n{origin_prompt}\n')

    origin_thread = client.beta.threads.create()
    origin_message = client.beta.threads.messages.create(
        thread_id=origin_thread.id,
        role="user",
        content=origin_prompt
    )
    origin_run = client.beta.threads.runs.create_and_poll(
        thread_id=origin_thread.id,
        assistant_id=code_assistant_id,
        instructions="Please generate workable streamlit code that can be run directly based on the user demand."
    )
    if origin_run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=origin_thread.id
        )
        #print(messages)
        response_text = messages.data[0].content[0].text.value
        #print(response_text)
    else:
        print(origin_run.status)

    response_text = match_content_in_quote(response_text, "```python", "```")

    print(f'token {i}.1 done, {origin_run.usage.prompt_tokens}, {origin_run.usage.completion_tokens}, {origin_run.usage.total_tokens}')


    #print(f'Code solution: \n{response_text}\n')

    with open(f'output/{i}/1.py', 'w', encoding='utf-8') as file:
        file.writelines(response_text)

    new_code_prompt = base_prompt + f"""Here is the user's request:
                  <user-query>
                  {tech_solution}
                  </user-query>
                  Generate the python code wrapped in python code block.
                  \n
                  """
    new_thread = client.beta.threads.create()
    new_message = client.beta.threads.messages.create(
        thread_id=new_thread.id,
        role="user",
        content=new_code_prompt
    )
    new_run = client.beta.threads.runs.create_and_poll(
        thread_id=new_thread.id,
        assistant_id=code_assistant_id,
        instructions="Please generate workable streamlit code that can be run directly based on the user demand."
    )
    if new_run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=new_thread.id
        )
        # print(messages)
        response_text = messages.data[0].content[0].text.value
        # print(response_text)
    else:
        print(new_run.status)

    print(f'token {i}.2 done, {new_run.usage.prompt_tokens}, {new_run.usage.completion_tokens}, {new_run.usage.total_tokens}')
    response_text = match_content_in_quote(response_text, "```python", "```")

    #print(f'Code solution: \n{response_text}\n')

    with open(f'output/{i}/2.py', 'w', encoding='utf-8') as file:
        file.writelines(response_text)