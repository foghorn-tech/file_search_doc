# Search

Search the web using a web crawler.

```python
import requests
from bs4 import BeautifulSoup

def search_duckduckgo(query):
    url = "https://duckduckgo.com/html/"
    params = {
        'q': query
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []

        for result in soup.find_all('a', class_='result__a'):
            title = result.get_text()
            link = result.get('href')
            results.append({'title': title, 'link': link})

        return results
    else:
        return None


if __name__ == "__main__":
    query = input("Enter search query: ")
    search_results = search_duckduckgo(query)

    if search_results:
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result['title']}\n   {result['link']}\n")
    else:
        print("Failed to retrieve results")
```