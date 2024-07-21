# jewels_service

## Summary



## Project Structure
````
jewels_service/
│
├── manage.py
├── jewels_service/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── jewels/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── authentication.py
│   ├── models.py
|   ├── permissions.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       └── __init__.py
└── requirements.txt

````

### Project Structure
user: user
password: user123456

### Project Runner
python manage.py runserver 0.0.0.0:8081

### Explanation of Tests
Fixtures:

api_client: Provides a DRF test client.
create_jewel: Creates a sample jewel for testing.
Tests:

test_list_jewels_with_valid_token: Tests listing jewels with a valid token.
test_list_jewels_without_token: Tests listing jewels without a token (public access).
test_create_jewel_with_valid_token: Tests creating a jewel with a valid token.
test_create_jewel_without_token: Tests creating a jewel without a token (should fail).
Mocking:

@patch('jewels.utils.verify_token'): Mocks the verify_token function to simulate token verification without making actual HTTP requests to the auth_service.

## Swagger
Swagger UI: http://localhost:8000/swagger/
Redoc UI: http://localhost:8000/redoc/