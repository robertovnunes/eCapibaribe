from src.db.schemas.model_schema import ModelSchema

class CategorySchema(ModelSchema):
    bson_type: str = "object"
    required: list = ["id", "name", "description", "keywords", "image_url", "itens"]
    properties: dict = {
        "id": {
            "bson_type": "string",
            "description": "The category's unique identifier"
        },
        "name": {
            "bson_type": "string",
            "description": "The category's name"
        },
        "description": {
            "bson_type": "string",
            "description": "The category's description"
        },
        "keywords": {
            "bson_type": "list",
            "description": "The category's keywords"
        },
        "image_url": {
            "bson_type": "string",
            "description": "The category's image_url"
        },
        "itens": {
            "bson_type": "list",
            "description": "The category's itens"
        }
    }

    def get(self) -> dict:
        return {
            "bson_type": self.bson_type,
            "required": self.required,
            "properties": self.properties
        }