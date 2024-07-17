import streamlit as st
import requests
from bs4 import BeautifulSoup
import json
import os
from openai import OpenAI

# Initialize the OpenAI Client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key>"))

# Function to perform web search using DuckDuckGo
def search_duckduckgo(query):
    url = "https://duckduckgo.com/html/"
    params = {'q': query}
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = [{'title': result.get_text(), 'link': result.get('href')} for result in soup.find_all('a', class_='result__a')]
        return results
    else:
        return None

# Streamlit app
st.title("AI Search Bot")

# User input
query = st.text_input("Enter your query:")

if query:
    # Perform web search
    search_results = search_duckduckgo(query)
    
    if search_results:
        # Save search results to a file
        with open('search_results.json', 'w') as f:
            json.dump(search_results, f)
        
        # Create a vector store and upload search results
        vector_store = client.beta.vector_stores.create(name="Search Results")
        file_stream = open("search_results.json", "rb")
        file_batch = client.beta.vector_stores.file_batches.upload_and_poll(vector_store_id=vector_store.id, files=[file_stream])
        
        # Create an assistant
        assistant = client.beta.assistants.create(
            name="Search Assistant",
            instructions="You are an AI search assistant. Use the search results to answer user queries.",
            model="gpt-4o",
            tools=[{"type": "code_interpreter"}, {"type": "vector_search"}]
        )
        
        # Create a conversation thread and add the user's query
        thread = client.beta.threads.create()
        message = client.beta.threads.messages.create(thread_id=thread.id, role="user", content=query)
        
        # Run the assistant
        run = client.beta.threads.runs.create_and_poll(thread_id=thread.id, assistant_id=assistant.id)
        
        # Display the results
        if run.status == 'completed':
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            st.write("Answer:", messages.data[0].content[0].text.value)
        else:
            st.write("Processing...")
    else:
        st.write("No search results found.")