# brave_search.py
# Demonstrates Brave-powered LLM-context web search for threat intel,
# using Brave Search API and OpenAI for contextualization.

import requests
import sys
import os
from openai import OpenAI

def search_brave(query):
    """Search using Brave Search API."""
    api_key = os.environ.get('BRAVE_API_KEY')
    if not api_key:
        raise ValueError("BRAVE_API_KEY environment variable not set.")
    
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {"X-Subscription-Token": api_key}
    params = {"q": query}
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    
    results = response.json().get('web', {}).get('results', [])
    return [result['title'] + ': ' + result['description'] for result in results[:3]]

def contextualize_with_llm(results, query):
    """Use OpenAI to contextualize search results."""
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set.")
    
    client = OpenAI(api_key=api_key)
    prompt = f"Contextualize these search results for the query '{query}': {results}"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python brave_search.py '<query>'")
        sys.exit(1)
    
    query = sys.argv[1]
    try:
        results = search_brave(query)
        if results:
            context = contextualize_with_llm(results, query)
            print("Search Results:")
            for r in results:
                print(f"- {r}")
            print(f"\nLLM Context: {context}")
        else:
            print("No results found.")
    except Exception as e:
        print(f"Error: {e}")
