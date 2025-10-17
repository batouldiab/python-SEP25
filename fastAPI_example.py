# ------------------------------------------------------------
# Setup & installation (run this in your terminal once):
#   pip install fastapi uvicorn
# ------------------------------------------------------------

# FastAPI is a Python framework for building web APIs.
# Think of an API as functions you can call over the internet.
from fastapi import FastAPI

# Create the web application object.
# We'll attach "routes" (like functions) to this app.
app = FastAPI()

# ---------------------- BASIC ROUTE -------------------------
# This defines an endpoint (URL path) that responds to a GET request.
# GET is used to "read" or "fetch" something.
# When someone goes to http://127.0.0.1:8000/ in a browser,
# FastAPI will run this function and return the result as JSON.
@app.get("/")
async def read_root():
    # FastAPI automatically converts Python dicts to JSON.
    return {"message": "Hello, World!"}

# ------------------------------------------------------------
# How to run the app (from your project folder in terminal):
#   uvicorn main:app --reload
#
# Explanation:
# - "main" is the Python filename without .py (main.py).
# - "app" is the FastAPI instance we created above.
# - "--reload" restarts the server automatically when you edit code.
# After running, open http://127.0.0.1:8000 in your browser.
# You can also see interactive docs at:
#   http://127.0.0.1:8000/docs  (Swagger UI)
#   http://127.0.0.1:8000/redoc (ReDoc)
# ------------------------------------------------------------

# Pydantic helps define data shapes and validate input automatically.
from pydantic import BaseModel

# This class describes what an "Item" looks like in requests/responses.
# It has two text fields: name and description.
# FastAPI uses this to validate incoming JSON and to generate docs.
class Item(BaseModel):
    name: str
    description: str

# We'll store items in a simple in-memory list for now.
# (In real apps, you'd use a database. This list resets when the app restarts.)
items = []

# ---------------------- CREATE ------------------------------
# POST is used to create new data on the server.
# Clients send JSON that matches the Item model in the request body.
@app.post("/items/")
async def create_item(item: Item):
    # "item" is already an Item object (validated by FastAPI/Pydantic).
    items.append(item)
    # Returning the item sends it back as JSON with the same fields.
    return item

# ---------------------- READ -------------------------------
# GET is used to fetch data. Here we return all stored items.
@app.get("/items/")
async def get_items():
    # FastAPI will convert the list of Item objects to JSON automatically.
    return items

# ---------------------- UPDATE -----------------------------
# PUT is used to fully replace an existing item at a known location.
# "{item_id}" is a "path parameter"—a variable part of the URL.
# Example request URL: /items/0  (updates the first item)
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    # Make sure the requested index exists in our list.
    if item_id < len(items):
        items[item_id] = item  # Replace the whole item
        return item
    # If the index is invalid, return an error message.
    # (In a real app, you’d return a proper HTTP status code like 404.)
    return {"error": "Item not found"}

# ---------------------- DELETE -----------------------------
# DELETE removes a specific item by its index in the list.
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id < len(items):
        # pop removes the item and returns it so we can show what was deleted.
        return items.pop(item_id)
    return {"error": "Item not found"}
