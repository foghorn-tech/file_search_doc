import streamlit as st
import openai
import requests
import json
import os
from sqlalchemy import create_engine
from bs4 import BeautifulSoup

# Initialize OpenAI client and set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to perform web search using DuckDuckGo
def search_duckduckgo(query):
    url = "https://duckduckgo.com/html/"
    params = {'q': query}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = [{'title': result.get_text(), 'link': result.get('href')} for result in soup.find_all('a', class_='result__a')]
        return results
    else:
        return None

# Function to save search results to a JSON file
def save_results_to_file(results, filename="search_results.json"):
    with open(filename, 'w') as file:
        json.dump(results, file)

# Function to create a vector store and upload search results
def create_vector_store_and_upload(file_path):
    client = openai.OpenAI()
    vector_store = client.beta.vector_stores.create(name="Search Results Store")
    file_stream = open(file_path, "rb")
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(vector_store_id=vector_store.id, files=[file_stream])
    return vector_store.id

# Function to create an assistant with code interpreter and vector search tools
def create_assistant(vector_store_id):
    client = openai.OpenAI()
    assistant = client.beta.assistants.create(
        instructions="You are an AI-powered search assistant. Retrieve and display search results based on user queries.",
        model="gpt-4o",
        tools=[{"type": "code_interpreter"}, {"type": "file_search"}],
        tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}}
    )
    return assistant

# Function to create a new conversation thread and add user's query
def create_thread_and_add_query(assistant, query):
    client = openai.OpenAI()
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(thread_id=thread.id, role="user", content=query)
    return thread

# Function to run the assistant and process the user's query
def run_assistant(assistant, thread):
    client = openai.OpenAI()
    run = client.beta.threads.runs.create_and_poll(thread_id=thread.id, assistant_id=assistant.id)
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        return messages.data[0].content[0].text.value
    else:
        return "Processing..."

# Streamlit app
st.title("AI-Powered Search Bot")

query = st.text_input("Enter your search query:")
if st.button("Search"):
    search_results = search_duckduckgo(query)
    if search_results:
        save_results_to_file(search_results)
        vector_store_id = create_vector_store_and_upload("search_results.json")
        assistant = create_assistant(vector_store_id)
        thread = create_thread_and_add_query(assistant, query)
        result = run_assistant(assistant, thread)
        st.write(result)
    else:
        st.write("Failed to retrieve results")