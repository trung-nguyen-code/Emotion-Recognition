from fastapi import FastAPI
from pydantic import BaseModel
from api.api import main_router

app = FastAPI(project_name="Emotion Recognition")
app.include_router(main_router)


class Item(BaseModel):
    name: str
    discount: int
    year: int
    price: int
    selling_price: int


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/items/")
async def add_item(item: Item) -> dict[str, int]:
    selling_price = item.price - item.discount
    return {"name": item.name, "selling_price": selling_price}
