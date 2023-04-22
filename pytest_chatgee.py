"""Pytest for ChatGee Server Root"""

import sys

from unittest.mock import MagicMock
import pytest

from chatgee.run_server import app

sys.path.insert(0, 'chatgee/')

@pytest.fixture
def client():
    """Create a test client for the app"""
    with app.test_client() as app_client:
        yield app_client

def test_prompt(app_client):
    """Test the '/prompt' route"""
    # Mock the ChatGeeOBJ class
    ChatGeeOBJ_mock = MagicMock()

    # Inject the mocked ChatGeeOBJ instance into the app's context
    app.config["ChatGee"] = ChatGeeOBJ_mock

    # Send a request to the app's '/prompt' route
    test_json = {
            "intent": {
                "id": "gatfjayew6ss8lkfzmsr7gxz",
                "name": "블록 이름"
            },
            "userRequest": {
                "timezone": "Asia/Seoul",
                "params": {
                "ignoreMe": "true"
                },
                "block": {
                "id": "gatfjayew6ss8lkfzmsr7gxz",
                "name": "블록 이름"
                },
                "user": {
                "id": "677903",
                "type": "accountId",
                "properties": {}
                }
            },
            "bot": {
                "id": "640458f126a0667a7b0d1873",
                "name": "봇 이름"
            },
            "action": {
                "name": "m6g1c3el8y",
                "params": {
                    "prompt": "test"
                },
                "id": "anhh1wxvcs426ebfvt937yam",
                "detailParams": {
                    "prompt": {
                        "origin": "test",
                        "value": "test",
                        "groupName": ""
                    }
                }
            }
        }

    response = app_client.post("/prompt", json=test_json)

    # Verify that the response is as expected
    assert response.status_code == 200
