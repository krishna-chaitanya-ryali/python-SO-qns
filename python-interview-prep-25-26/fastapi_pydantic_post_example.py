"""
Problem:
--------
Create a FastAPI POST endpoint that accepts request data using a Pydantic model
and returns a response.

This example demonstrates:
- FastAPI application setup
- Request validation using Pydantic
- Asynchronous API endpoint
"""

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    """
    Pydantic model for request body validation.
    """
    name: str
    description: str


app = FastAPI(title="FastAPI Pydantic Example")


@app.post("/items/")
async def create_item(item: Item):
    """
    Creates a new item.

    Args:
        item (Item): Item data received in request body.

    Returns:
        dict: Confirmation message along with item details.
    """
    return {
        "message": "Item created successfully",
        "item": item
    }


"""
Example Request:
----------------
POST /items/
Content-Type: application/json

{
    "name": "Laptop",
    "description": "FastAPI interview example"
}

Example Response:
-----------------
{
    "message": "Item created successfully",
    "item": {
        "name": "Laptop",
        "description": "FastAPI interview example"
    }
}

How to Run:
-----------
1. Install dependencies:
   pip install fastapi uvicorn

2. Run the application:
   uvicorn fastapi_pydantic_post_example:app --reload

3. Open Swagger UI:
   http://127.0.0.1:8000/docs
   
   FastAPI uses Pydantic models to validate incoming request data automatically.
The request body is parsed into the Item model, ensuring type safety and validation.
FastAPI also auto-generates interactive API documentation using Swagger.
"""
