import sys
from pathlib import Path

from fastapi.testclient import TestClient

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from app.main import app, settings

client = TestClient(app)
prefix = settings.API_V1_STR


def test_health_endpoint():
    url = f"{prefix}/health"
    response = client.get(url=url)
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}


def test_encode_endpoint():
    text = "This is an example sentence"
    url = f"{prefix}/encode?sentence={text}"
    response = client.post(url=url)
    assert response.status_code == 200
    output = response.json()
    assert type(output) == list
    assert len(output) == 500
