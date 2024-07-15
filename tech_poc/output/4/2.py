import streamlit as st
import pandas as pd

def csv_to_markdown_table(csv_file):
    df = pd.read_csv(csv_file)
    markdown_table = df.to_markdown(index=False)
    return markdown_table

st.title("CSV to Markdown Converter for Obsidian")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    markdown_table = csv_to_markdown_table(uploaded_file)
    st.markdown("### Markdown Table")
    st.code(markdown_table, language='markdown')
    st.markdown("Copy the above Markdown table and paste it into your Obsidian note.")