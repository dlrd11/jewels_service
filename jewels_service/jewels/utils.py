import json

import requests
from rest_framework import exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication

# AUTH_SERVICE_URL = "http://0.0.0.0:8000/auth/verify"
AUTH_SERVICE_URL = "https://web-production-e9b0.up.railway.app/auth/verify"


def verify_token(token):
    decoded_token = token.decode('utf-8')
    try:
        response = requests.post(
            AUTH_SERVICE_URL,
            json={'access_token': decoded_token},
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise exceptions.AuthenticationFailed('Failed to verify token')


