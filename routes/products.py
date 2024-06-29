from fastapi import APIRouter, Form, UploadFile, File
from typing import List
from database.connections import Database
from models.products import Product

product_router = APIRouter(tags=["Products"])
product_database = Database(Product)


@product_router.get("/", response_model=List[Product])
async def get_all_products() -> List[Product]:
    products = await product_database.get_all()
    return products


@product_router.post("/create")
async def create_product(
        name: str = Form(...),
        category: str = Form(...),
        description: str = Form(...),
        image1: UploadFile = File(...),
        image2: UploadFile = File(...)

) -> dict:
    image1_data = await image1.read()
    image2_data = await image2.read()
    body = Product(
        name=name,
        category=category,
        description=description,
        image1=image1_data,
        image2=image2_data
    )
    await product_database.save(body)
    return {
        "message": "product created successfully!!!"
    }
