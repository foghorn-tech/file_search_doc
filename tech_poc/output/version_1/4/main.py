import streamlit as st
import pandas as pd

st.title("CSV to Obsidian Import Guide")

st.markdown("""
### Steps to Import a CSV File into Obsidian

1. **Prepare the CSV File**: Ensure your CSV file is properly formatted and saved on your local machine.
2. **Open Obsidian**: Launch the Obsidian application on your computer.
3. **Install the CSV Plugin**: If not already installed, navigate to the Obsidian settings, go to the "Community plugins" section, and search for a CSV import plugin. Install and enable the plugin.
4. **Create a New Note**: In Obsidian, create a new note where you want to import the CSV data.
5. **Use the CSV Plugin**: Use the installed CSV plugin to import the CSV file. This typically involves selecting an option like "Import CSV" from the plugin's menu and then choosing the CSV file from your local machine.
6. **Verify the Import**: Check the new note to ensure that the CSV data has been imported correctly. Adjust any formatting as needed.
7. **Save and Organize**: Save the note and organize it within your Obsidian vault as desired.
""")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of CSV Data")
    st.write(df)