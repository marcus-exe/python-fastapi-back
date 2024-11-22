from fastapi import FastAPI

# Create an instance of the FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Path parameter example
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

# POST example
@app.post("/create-item/")
def create_item(name: str, price: float, in_stock: bool = True):
    return {"name": name, "price": price, "in_stock": in_stock}

# Run with: uvicorn filename:app --reload
