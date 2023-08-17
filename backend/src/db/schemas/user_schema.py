from src.db.schemas.model_schema import ModelSchema


class UserSchema(ModelSchema):
    bson_type: str = "object"
    required: list = ["id", "name", "email", "password", "cpf"]
    properties: dict = {
        "id": {
            "bson_type": "string",
            "description": "The user's unique identifier"
        },
        "name": {
            "bson_type": "string",
            "description": "The user's name"
        },
        "email": {
            "bson_type": "string",
            "description": "The user's e-mail"
        },
        "password": {
            "bson_type": "string",
            "description": "The user's password"
        },
        "cpf": {
            "bson_type": "string",
            "description": "The user's CPF"
        },
    }

    def get(self) -> dict:
        return {
            "bson_type": self.bson_type,
            "required": self.required,
            "properties": self.properties
        }