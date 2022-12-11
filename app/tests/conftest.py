import pytest
from fastapi.testclient import TestClient
from app.trystack import app 


client = TestClient(app)

@pytest.fixture
def app():
     return app()

@pytest.fixture()
def client():
     return client