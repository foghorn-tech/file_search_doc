import streamlit as st
import requests
from bs4 import BeautifulSoup
import json
from openai import OpenAI

# Initialize the OpenAI Client
client = OpenAI(api_key=st.secrets["openai_api_key"])

# Function to search using DuckDuckGo
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

query = st.text_input("Enter your search query:")

if st.button("Search"):
    if query:
        # Search using DuckDuckGo
        search_results = search_duckduckgo(query)
        
        if search_results:
            # Save search results to a JSON file
            with open("search_results.json", "w") as file:
                json.dump(search_results, file)
            
            # Create a vector store
            vector_store = client.beta.vector_stores.create(name="SearchResults")
            
            # Upload search results to vector store
            file_stream = open("search_results.json", "rb")
            file_batch = client.beta.vector_stores.file_batches.upload_and_poll(vector_store_id=vector_store.id, files=[file_stream])
            
            # Create an assistant with code interpreter and vector search tools
            assistant = client.beta.assistants.create(
                instructions="You are an AI search assistant. Use the vector store to answer search queries.",
                model="gpt-4o",
                tools=[{"type": "code_interpreter"}, {"type": "vector_search"}],
                tool_resources={"vector_search": {"vector_store_ids": [vector_store.id]}}
            )
            
            # Create a conversation thread
            thread = client.beta.threads.create(messages=[{"role": "user", "content": query}])
            
            # Add user's query to the thread
            client.beta.threads.messages.create(thread_id=thread.id, role="user", content=query)
            
            # Run the assistant to process the query
            run = client.beta.threads.runs.create_and_poll(thread_id=thread.id, assistant_id=assistant.id)
            
            # Display the results
            if run.status == 'completed':
                messages = client.beta.threads.messages.list(thread_id=thread.id)
                st.write(messages.data[0].content)
            else:
                st.write("Processing...")
        else:
            st.write("No results found.")
    else:
        st.write("Please enter a query.")