import streamlit as st
from openai import OpenAI
import os
import requests
import json

# Initialize OpenAI Client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key>"))

# Integrate Web Search API
def search_web(query):
    api_key = "YOUR_SEARCH_API_KEY"
    search_engine_id = "YOUR_SEARCH_ENGINE_ID"
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}"
    response = requests.get(url)
    return response.json()

# Process Search Results
def process_search_results(results):
    processed_results = []
    for item in results.get('items', []):
        processed_results.append({
            'title': item['title'],
            'link': item['link'],
            'snippet': item['snippet']
        })
    return processed_results

# Create Vector Store for Search Results
vector_store = client.beta.vector_stores.create(name="SearchResults")

# Upload Search Results to Vector Store
def upload_to_vector_store(results):
    file_path = "search_results.json"
    with open(file_path, 'w') as f:
        json.dump(results, f)
    file_stream = open(file_path, "rb")
    client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id, files=[file_stream]
    )

# Create Assistant with Code Interpreter and Vector Search Tools
assistant = client.beta.assistants.create(
    name="SearchBot",
    instructions="You are an AI search bot. Use the vector store to find relevant information based on user queries.",
    model="gpt-4o",
    tools=[{"type": "code_interpreter"}, {"type": "vector_search"}]
)

# Create a New Conversation Thread
thread = client.beta.threads.create(assistant_id=assistant.id)

# Add User Query to Conversation Thread
def add_query_to_thread(query):
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=query
    )

# Run Assistant to Process User Query
response = client.beta.threads.runs.create(thread_id=thread.id)

# Display Results
def display_results(response):
    for message in response['messages']:
        st.write(message['content'])

# Streamlit App
st.title("AI Search Bot")

query = st.text_input("Enter your query:")
if st.button("Search"):
    search_results = search_web(query)
    processed_results = process_search_results(search_results)
    upload_to_vector_store(processed_results)
    add_query_to_thread(query)
    response = client.beta.threads.runs.create(thread_id=thread.id)
    display_results(response)