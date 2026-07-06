# file konfigurasi ini masih memakai app.main_ram

import pytest
from fastapi.testclient import TestClient
from app.main_db import app
from app.database import reset_db

@pytest.fixture(autouse=True)
def client():
    reset_db()
    return TestClient(app)