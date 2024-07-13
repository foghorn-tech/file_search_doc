def match_content_in_quote(content: str, start_quote: str, end_quote: str):
    start_index = content.find(start_quote)

    if start_index != -1:
        # Adjust start_index to get the start of the actual content, not the marker
        start_index += len(start_quote)
        end_index = content.find(end_quote, start_index)

        if end_index != -1:
            # Extract the content between the quotes without including the end marker
            return content[start_index:end_index].strip()

    return ""
