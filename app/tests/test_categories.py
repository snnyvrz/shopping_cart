from fastapi.testclient import TestClient

from .. import main

client = TestClient(main.app)


def test_get_all_categories():
    response = client.get("/categories/")
    assert response.status_code == 200
