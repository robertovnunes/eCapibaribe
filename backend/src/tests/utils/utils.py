from fastapi.testclient import TestClient


def req_type_to_function(client: TestClient, req_type: str):
    return {
        "GET": client.get,
        "POST": client.post,
        "PUT": client.put,
        "DELETE": client.delete
    }[req_type]


def get_data_response(response):
    return response.json()["data"]

