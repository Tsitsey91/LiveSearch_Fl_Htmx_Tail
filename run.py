import time
from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data to simulate a database with 30 items
items = [
    {"id": i, "name": f"Item {i}", "description": f"Description for Item {i}"}
    for i in range(1, 31)
]

def paginate_items(items, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    return items[start:end]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    time.sleep(1)  # Introduce a 2-second delay to simulate a slow response
    
    query = request.args.get('query', '').lower()
    page = int(request.args.get('page', 1))
    per_page = 10

    if query:
        filtered_items = [item for item in items if query in item['name'].lower() or query in item['description'].lower()]
    else:
        filtered_items = items

    paginated_items = paginate_items(filtered_items, page, per_page)
    total_pages = (len(filtered_items) + per_page - 1) // per_page

    return render_template('results.html', 
                           results=paginated_items, 
                           page=page, 
                           total_pages=total_pages, 
                           query=query)

if __name__ == '__main__':
    app.run(debug=True)
