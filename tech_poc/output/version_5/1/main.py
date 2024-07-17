import streamlit as st
import openai
import requests
import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from openai.embeddings_utils import get_embedding, cosine_similarity

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to perform web search using Bing Search API
def perform_web_search(query):
    subscription_key = os.getenv("BING_SEARCH_API_KEY")
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    return search_results

# Function to save search results to a JSON file
def save_search_results_to_file(search_results, filename="search_results.json"):
    with open(filename, "w") as f:
        json.dump(search_results, f)

# Function to create a vector store and upload search results
def create_vector_store_and_upload(filename="search_results.json"):
    with open(filename, "r") as f:
        search_results = json.load(f)
    
    vectors = []
    for result in search_results["webPages"]["value"]:
        text = result["snippet"]
        embedding = get_embedding(text, engine="text-embedding-ada-002")
        vectors.append({"text": text, "embedding": embedding})
    
    # Save vectors to a file
    with open("vectors.json", "w") as f:
        json.dump(vectors, f)

# Function to create an AI assistant
def create_ai_assistant():
    def assistant(query):
        # Load vectors
        with open("vectors.json", "r") as f:
            vectors = json.load(f)
        
        # Get query embedding
        query_embedding = get_embedding(query, engine="text-embedding-ada-002")
        
        # Find the most similar result
        similarities = [cosine_similarity(query_embedding, v["embedding"]) for v in vectors]
        most_similar_index = similarities.index(max(similarities))
        most_similar_result = vectors[most_similar_index]["text"]
        
        return most_similar_result
    
    return assistant

# Streamlit app
st.title("AI Search Bot")

# User query input
user_query = st.text_input("Enter your query:")

if user_query:
    # Perform web search
    search_results = perform_web_search(user_query)
    
    # Save search results to file
    save_search_results_to_file(search_results)
    
    # Create vector store and upload search results
    create_vector_store_and_upload()
    
    # Create AI assistant
    ai_assistant = create_ai_assistant()
    
    # Get assistant response
    response = ai_assistant(user_query)
    
    # Display the results
    st.write("Search Results:")
    st.write(response)