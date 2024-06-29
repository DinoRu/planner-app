from typing import Optional

from beanie import Document


class Product(Document):
    name: str
    category: str
    description: str
    image1: Optional[bytes] = None
    image2: Optional[bytes] = None

    # class Config:
    #     json_schema_extra = {
    #         "title": "Product",
    #         "description": "A model representing a product with its details and images.",
    #         "examples": {
    #             "example1": {
    #                 "summary": "A sample product",
    #                 "description": "This is an example of a product with all fields filled.",
    #                 "value": {
    #                     "name": "Sample Product",
    #                     "category": "Electronics",
    #                     "description": "A sample product used for demonstration purposes.",
    #                     "image1": "base64encodedstring1",
    #                     "image2": "base64encodedstring2"
    #                 }
    #             },
    #         }
    #     }