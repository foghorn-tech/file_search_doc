# Code Interpreter

How to create an assistant with Code Interpreter tool.

1. Initialize OpenAI client
```python
# Initialize OpenAI client
client = OpenAI(api_key=api_key)
```
2. Upload file or image to OpenAI, if required
```python
file = client.files.create(file=uploaded_file,purpose='assistants')
```

3. Create an assistant with Code Interpreter tool(if you have files to analyze, please upload them first)
```python
assistant = client.beta.assistants.create(
    instructions="You are a data analysis assistant. Analyze the data and provide insights.",
    model="gpt-4o",
    tools=[{"type": "code_interpreter"}],
    tool_resources={
        "code_interpreter": {
            "file_ids": [file.id]
        }
    }
)
```
4. Run the assistant with the user's query
```python
 # Create a thread and add the user's query
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": analysis_query,
            "attachments": [
                {
                    "file_id": file.id,
                    "tools": [{"type": "code_interpreter"}]
                }
            ]
        }
    ]
)
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id
)
```
5. Display the results of the analysis, which could be in the form of text or charts

```python
if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    result = messages.data[0].content[0].text.value
    st.write(result)

    # Display charts if any
    if "chart" in result:
        chart_data = pd.DataFrame(eval(result.split("chart:")[1]))
        chart = alt.Chart(chart_data).mark_line().encode(
            x='x:Q',
            y='y:Q'
        )
        st.altair_chart(chart, use_container_width=True)
else:
    st.write("Analysis in progress, please wait...")
```
