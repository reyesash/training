import copy
import pytest
from fastapi.testclient import TestClient
from importlib import import_module

# Import the app module and snapshot initial activities state
app_module = import_module("src.app")
app = app_module.app
_initial_activities = copy.deepcopy(app_module.activities)


@pytest.fixture
def client():
    # Reset in-memory activities to the initial state before each test
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(_initial_activities))
    with TestClient(app) as c:
        yield c
