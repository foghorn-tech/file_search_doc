from openai import OpenAI


def get_tech_solution(client : OpenAI, query: str, rewrite_assistant_id: str):

    prompt = """You are an expert in technology, specializing in prompt fine-tuning and technical solution design.
                Your responsibility is to rewrite the user's request into a more detailed technical solution.\n"""

    prompt += f"""Here is the user's request:
                   <user-query>
                   {query}
                   </user-query>
                  Rewrite the user's request into a concise, clear technical solution. Present the solution in a step-by-step format. Provide only the improved version without comparisons, additional information, or code.
                   """

    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
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
        # print(messages)
        response_text = messages.data[0].content[0].text.value
        # print(response_text)
    else:
        print(run.status)

    return response_text