import pytest
from fastapi.testclient import TestClient
from typing import Generator
from backend.src.create_user.create_user import cadastro, ROOT

pytest_plugins = "pytester"

@pytest.fixture(scope="function")
def client() -> Generator:
    """
    Create a test client for the FastAPI app.
    """
    with TestClient(cadastro) as c:
        yield c

@pytest.fixture
def context():
    """
    Variable to store context data between steps.
    Note: remember to always return the context variable at the end of the each steps.
    """
    b = {}
    yield b