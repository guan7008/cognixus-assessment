import requests


def test_add_todo_no_header():
    endpoint = "http://localhost:8000/api/v1/data/todo"
    response = requests.post(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert "status_code" in json
    assert "message" in json
    assert json["status_code"] == 20001
    assert json["message"] == "ERROR: Unauthorized"


def test_add_todo_no_data():
    endpoint = "http://localhost:8000/api/v1/data/todo"
    response = requests.post(
        endpoint,
        headers={
            "x-api-key": "5cebc2dc-894e-4ce9-ae13-e446c348f7e6",
        },
    )
    assert response.status_code == 200
    json = response.json()
    assert "status_code" in json
    assert "message" in json
    assert json["status_code"] == 21001
    assert json["message"] == "ERROR: Invalid Input"


def test_add_todo_complete():
    endpoint = "http://localhost:8000/api/v1/data/todo"
    response = requests.post(
        endpoint,
        data={"task": "testing123"},
        headers={
            "x-api-key": "5cebc2dc-894e-4ce9-ae13-e446c348f7e6",
        },
    )
    assert response.status_code == 200
    json = response.json()
    assert "status_code" in json
    assert "message" in json
    assert json["status_code"] == 22002
    assert json["message"] == "OK: Add a TODO item"


def test_delete_todo_no_header():
    endpoint = "http://localhost:8000/api/v1/data/todo/1"
    response = requests.delete(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert "status_code" in json
    assert "message" in json
    assert json["status_code"] == 20001
    assert json["message"] == "ERROR: Unauthorized"


def test_add_todo_complete():
    endpoint = "http://localhost:8000/api/v1/data/todo/1"
    response = requests.delete(
        endpoint,
        headers={
            "x-api-key": "5cebc2dc-894e-4ce9-ae13-e446c348f7e6",
        },
    )
    assert response.status_code == 200
    json = response.json()
    assert "status_code" in json
    assert "message" in json
    assert json["status_code"] == 22004
    assert json["message"] == "OK: Delete a TODO item"


def test_list_todo_no_header():
    endpoint = "http://localhost:8000/api/v1/data/todo"
    response = requests.get(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert "status_code" in json
    assert "message" in json
    assert json["status_code"] == 20001
    assert json["message"] == "ERROR: Unauthorized"


def test_list_todo_default():
    endpoint = "http://localhost:8000/api/v1/data/todo"
    response = requests.get(
        endpoint,
        headers={
            "x-api-key": "5cebc2dc-894e-4ce9-ae13-e446c348f7e6",
        },
    )
    assert response.status_code == 200
    json = response.json()
    assert "status_code" in json
    assert "message" in json
    assert json["status_code"] == 22000
    assert json["message"] == "OK: List all TODO items"


def test_list_todo_complete():
    endpoint = "http://localhost:8000/api/v1/data/todo"
    response = requests.get(
        endpoint,
        data={"limit": 5, "offset": 1},
        headers={
            "x-api-key": "5cebc2dc-894e-4ce9-ae13-e446c348f7e6",
        },
    )
    assert response.status_code == 200
    json = response.json()
    assert "status_code" in json
    assert "message" in json
    assert json["status_code"] == 22000
    assert json["message"] == "OK: List all TODO items"

def test_mark_completed_todo_no_header():
    endpoint = "http://localhost:8000/api/v1/data/todo/1/completed"
    response = requests.put(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert "status_code" in json
    assert "message" in json
    assert json["status_code"] == 20001
    assert json["message"] == "ERROR: Unauthorized"


def test_mark_completed_todo_complete():
    endpoint = "http://localhost:8000/api/v1/data/todo/1/completed"
    response = requests.put(
        endpoint,
        headers={
            "x-api-key": "5cebc2dc-894e-4ce9-ae13-e446c348f7e6",
        },
    )
    assert response.status_code == 200
    json = response.json()
    assert "status_code" in json
    assert "message" in json
    assert json["status_code"] == 22006
    assert json["message"] == "OK: Mark completed a TODO item"
