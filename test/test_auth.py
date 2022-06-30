import os
import requests


def test_google_login_no_header(api_v1_host):
    endpoint = os.path.join(api_v1_host, "auth", "google", "login")
    response = requests.post(endpoint)
    assert response.status_code == 401
