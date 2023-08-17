def user_entity(category) -> dict:
    """
    Returns a dict of the item entity
    """
    return {
        "name": category["name"],
        "email": category["email"],
        "password": category["password"],
        "cpf": category["cpf"]
    }

def user_response_entity(category) -> dict:
    """
    Returns a dict of the item response entity
    """
    return {
        "id": category["id"],
        "name": category["name"],
        "email": category["email"],
        "password": category["password"],
        "cpf": category["cpf"]
    }

def use_list_entity(users) -> list:
    """
    Returns a list of the item entity
    """
    return [user_entity(user) for user in users]