# jewels_service

## Summary

This project provides a REST API service to manage jewels. The API system enable CRUD operations and it's working with authentication JWT. 

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
## Instalation

1. Clone the repository:

   ```bash
   git clone https://github.com/tu_usuario/jewels_service.git
   cd jewels_service
2. Create and activate a virtual environment:
   ```bash
      python -m venv env
      source env/bin/activate   # In Windows: env\Scripts\activate

3. Install the dependencies
   ```bash
   pip install -r requirements.txt

## Configuration
1. Config the environment variables in the file .env (optional):
   ```bash
   pip install -r requirements.txt
2. Config the database in `settings.py` if you don't want to use SQLite
3. Make migrations of database
   ```bash
   python manage.py migrate

## Project Runner
   ```bash
      python manage.py runserver 0.0.0.0:8081
  ```
### Executing with Docker 
   ```bash
      docker-compose up --build
   ```


## API Documentation
Swagger UI: http://localhost:8081/swagger/
Redoc UI: http://localhost:8081/redoc/

## How to use
The API uses JWT for authentication. To access protected endpoints, you must include the JWT token in the request headers.
   ``bash
      Authorization: Bearer your_jwt_token

### Use case
   Access token
   ```bash
      curl -X POST http://localhost:8080/auth/login \
         -H "Content-Type: application/json" \
         -d '{"username": "your_user", "password": "tu_contraseña"}'
```
----------------------
   Create a jewel
   ```bash
      curl -X POST http://localhost:8081/api/jewels/ \
     -H "Authorization: Bearer your_jwt_token" \
     -H "Content-Type: application/json" \
     -d '{"name": "Diamond Ring", "description": "A beautiful diamond ring", "price": "5000.00"}'

   ```
-----------------------
   Retrieve a list of jewels
   ```bash
   curl -X GET http://localhost:8081/api/jewels/ \
     -H "Authorization: Bearer your_jwt_token"

   ```

### License
This project is licence over MIT.

This `README.md` includes sections on installation, configuration, running the server, API documentation, usage examples and contributions. This should provide a complete guide for other developers who wish to use or contribute to your project.
