import requests


def test_google_login_no_header():
    endpoint = "http://localhost:8000/api/v1/auth/google/login"
    response = requests.post(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert "status_code" in json
    assert "message" in json
    assert json["status_code"] == 20001
    assert json["message"] == "ERROR: Unauthorized"


def test_google_login_no_data():
    endpoint = "http://localhost:8000/api/v1/auth/google/login"
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


def test_google_login_complete():
    endpoint = "http://localhost:8000/api/v1/auth/google/login"
    response = requests.post(
        endpoint,
        data={"redirect_uri": "http://localhost:8000/google/auth"},
        headers={
            "x-api-key": "5cebc2dc-894e-4ce9-ae13-e446c348f7e6",
        },
    )
    assert response.status_code == 200
    json = response.json()
    assert "status_code" in json
    assert "message" in json
    assert "redirect_uri" in json
    assert json["status_code"] == 20000
    assert json["message"] == "OK: Proceed To Login Uri"
