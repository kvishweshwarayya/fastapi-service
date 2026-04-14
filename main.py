from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse

#uvicorn main:app --reload

app = FastAPI()

# Data model for POST requests
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/favicon.ico")
def favicon():
    return FileResponse("favicon.ico")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Container!"}

# 1. Path Parameter: Fetch a specific item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "status": "found"}

# 2. Query Parameters: Filter results (e.g., /search?q=phone&limit=10)
@app.get("/search")
def search_items(q: str = None, limit: int = 10):
    return {"query": q, "limit": limit, "results": []}

# 3. POST Request: Create a new item using a JSON body
@app.post("/items")
def create_item(item: Item):
    return {"message": f"Item {item.name} created", "data": item}

# 4. PUT Request: Update an existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated_name": item.name}
