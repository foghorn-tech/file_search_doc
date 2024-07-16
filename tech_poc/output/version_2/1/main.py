import streamlit as st
from openai import OpenAI
import os
import requests
import json

# Initialize OpenAI Client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key>"))

# Perform Web Search
def search_web(query):
    url = "https://api.example.com/search"
    params = {'q': query, 'api_key': 'your_search_api_key'}
    response = requests.get(url, params=params)
    return response.json()

# Save Search Results
def save_results(results, filename="search_results.json"):
    with open(filename, 'w') as file:
        json.dump(results, file)

# Streamlit App
st.title("AI Search Bot")

query = st.text_input("Enter your query:")

if st.button("Search"):
    if query:
        # Perform web search
        results = search_web(query)
        
        # Save results to file
        save_results(results)
        
        # Upload Search Results to OpenAI
        file = client.files.create(file=open("search_results.json", "rb"), purpose="fine-tune")
        
        # Create Vector Store
        vector_store = client.beta.vector_stores.create(name="Search Results Store")
        file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store.id, files=[open("search_results.json", "rb")]
        )
        
        # Create Assistant with Vector Search Tool
        assistant = client.beta.assistants.create(
            name="Search Assistant",
            instructions="You are an AI search assistant. Use the search results to answer user queries.",
            model="gpt-4o",
            tools=[{"type": "code_interpreter"}, {"type": "vector_search"}],
            tool_resources={"vector_search": {"vector_store_ids": [vector_store.id]}}
        )
        
        # Create Conversation Thread
        thread = client.beta.threads.create()
        
        # Add User Query to Thread
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=query
        )
        
        # Run Assistant to Process Query
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id
        )
        
        # Display Results
        if run.status == 'completed':
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            result = messages.data[0].content[0].text.value
            st.write(result)
        else:
            st.write("Processing, please wait...")