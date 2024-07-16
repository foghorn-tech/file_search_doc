import streamlit as st
import openai
import requests
import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from openai.embeddings_utils import get_embedding, cosine_similarity

# Initialize the OpenAI client and set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to perform web search using Bing Search API
def web_search(query):
    subscription_key = os.getenv("BING_SEARCH_API_KEY")
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    return search_results

# Function to parse and store search results
def parse_search_results(search_results):
    parsed_results = []
    for result in search_results.get("webPages", {}).get("value", []):
        parsed_results.append({
            "name": result["name"],
            "url": result["url"],
            "snippet": result["snippet"]
        })
    return parsed_results

# Function to create a vector store
def create_vector_store(parsed_results):
    vectors = []
    for result in parsed_results:
        embedding = get_embedding(result["snippet"], engine="text-embedding-ada-002")
        vectors.append({"result": result, "embedding": embedding})
    return vectors

# Function to upload search results to OpenAI's vector store
def upload_to_vector_store(vectors):
    # This is a placeholder function. Replace with actual implementation to upload to OpenAI's vector store.
    pass

# Function to process user query and retrieve relevant search results
def process_query(user_query, vectors):
    query_embedding = get_embedding(user_query, engine="text-embedding-ada-002")
    similarities = [(cosine_similarity(query_embedding, vector["embedding"]), vector["result"]) for vector in vectors]
    similarities.sort(reverse=True, key=lambda x: x[0])
    return [result for _, result in similarities[:5]]

# Streamlit app
st.title("AI-powered Search Bot")

user_query = st.text_input("Enter your search query:")

if user_query:
    search_results = web_search(user_query)
    parsed_results = parse_search_results(search_results)
    vectors = create_vector_store(parsed_results)
    upload_to_vector_store(vectors)
    relevant_results = process_query(user_query, vectors)
    
    st.write("Search Results:")
    for result in relevant_results:
        st.write(f"**{result['name']}**")
        st.write(result["snippet"])
        st.write(result["url"])