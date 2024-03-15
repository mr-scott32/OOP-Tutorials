import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_books():
    search_query = "science fiction"
    limit = 10  # Retrieve 10 results

    url = f"https://openlibrary.org/search.json?q={search_query}&limit={limit}"

    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = json.loads(response.content)
            books = data.get("docs", [])  # Handle potential errors with "get"
            return render_template('books.html', books=books)
            # place the response in a new json file
            with open("books.json", "w") as file:
                json.dump(data, file, indent=2)
        except json.JSONDecodeError as e:
            return f"Error: Failed to decode JSON response. {e}"
    else:
        return f"Error: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
