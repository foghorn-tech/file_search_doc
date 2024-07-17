import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL"),
)

## Create a new assistant: for write code
# assistant = client.beta.assistants.create(
#   name="Coding Assistant",
#   instructions="You are a coding assistant build data app using streamlit, skilled in coding in python and streamlit.",
#   model="gpt-4o",
#   tools=[{"type": "file_search"}],
#   temperature=0.1
# )
# print(assistant)
code_assistant_id = 'asst_4VuT8MH3frdp33CSAF8fMYpd'



vector_store = client.beta.vector_stores.create(name="openai docs test")

base_directories = ['../api', '../tech_solution']
file_paths = []
for base_directory in base_directories:
    for dir_path, dir_names, filenames in os.walk(base_directory):
        for filename in filenames:
            file_paths.append(os.path.join(dir_path, filename))
file_streams = [open(path, "rb") for path in file_paths]

# Use the upload and poll SDK helper to upload the files, add them to the vector store,
# and poll the status of the file batch for completion.
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
  vector_store_id=vector_store.id, files=file_streams
)

assistant = client.beta.assistants.update(
  assistant_id=code_assistant_id,
  tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

print(code_assistant_id)
print(vector_store.id)
