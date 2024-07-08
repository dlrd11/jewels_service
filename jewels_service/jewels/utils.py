import requests

AUTH_SERVICE_URL = "http://0.0.0.0:8000/auth/login"


def verify_token(token):
    try:
        response = requests.post(
            AUTH_SERVICE_URL,
            headers={'Authorization': f'Bearer {token}'}
        )
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False
