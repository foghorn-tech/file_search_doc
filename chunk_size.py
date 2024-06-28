import os

import tiktoken

def num_tokens_from_string(string: str, encoding) -> int:
    """Returns the number of tokens in a text string."""
    num_tokens = len(encoding.encode(string))
    return num_tokens

encoding = tiktoken.encoding_for_model("gpt-4o")

directories = ['open-ai-doc/output', 'streamlit-doc/output']
file_paths = []
for directory in directories:
    for dirpath, dirnames, filenames in os.walk(directory):
        file_paths.extend([os.path.join(dirpath, file) for file in filenames])



for file_path in file_paths:
    with open(file_path, "r") as file:
        text = file.read()
        num_tokens = num_tokens_from_string(text, encoding)
        if num_tokens > 400:
            print(f"{file_path}: {num_tokens} tokens")