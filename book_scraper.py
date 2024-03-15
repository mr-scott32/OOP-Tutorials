import requests
import json
import flask

search_query = "science fiction"
limit = 10  # Retrieve 10 results

url = f"https://openlibrary.org/search.json?q={search_query}&limit={limit}"

response = requests.get(url)

if response.status_code == 200:
  # Check for empty response content
  if response.content:
    try:
      data = json.loads(response.content)
      # Check for API errors within the JSON data (optional)
      if data.get("error"):
        print("API Error:", data.get("error"))
      else:
        books = data.get("docs", [])  # Handle potential errors with "get"

        for book in books:
          title = book.get("title", None)
          author_data = book.get("author_name", [])  
          # Extract first author from the list (might have multiple)
          author = author_data[0] if author_data else None
          
          print(f"Title: {title}, Author: {author}")
    except json.JSONDecodeError as e:
      print("Error: Failed to decode JSON response.")
      print(e)
  else:
    print("Warning: Empty response received from API.")
else:
  print("Error:", response.status_code)

#place the response in a new json file
with open("books.json", "w") as file:
    json.dump(data, file, indent=2)

  