import os

import tiktoken

def num_tokens_from_string(string: str, encoding) -> int:
    """Returns the number of tokens in a text string."""
    num_tokens = len(encoding.encode(string))
    return num_tokens

encoding = tiktoken.encoding_for_model("gpt-4o")
file_paths = [f'open-ai-doc/output/{file}' for file in os.listdir('open-ai-doc/output')]


for file_path in file_paths:
    with open(file_path, "r") as file:
        text = file.read()
        num_tokens = num_tokens_from_string(text, encoding)
        print(f"{file_path}: {num_tokens}")