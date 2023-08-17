def category_entity(category) -> dict:
    """
    Returns a dict of the item entity
    """
    return {
        "name": category["name"],
        "description": category["description"],
        "keywords": category["keywords"],
        "image_url": category["image_url"],
    }

def category_response_entity(category) -> dict:
    """
    Returns a dict of the item response entity
    """
    return {
        "id": category["id"],
        "name": category["name"],
        "description": category["description"],
        "keywords": category["keywords"],
        "image_url": category["image_url"],
    }

def category_list_entity(categories) -> list:
    """
    Returns a list of the item entity
    """
    return [category_entity(category) for category in categories]