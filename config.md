create a django project
    django-admin startproject jewels_service
    cd jewels_service
Create the Jewels App:
    python manage.py startapp jewels
Install Dependencies:
    pip install -r requirements.txt
Add Installed Apps
    Add rest_framework, rest_framework_simplejwt, and jewels to the INSTALLED_APPS in jewels_service/settings.py.    
    INSTALLED_APPS = [
        'rest_framework',
        'rest_framework_simplejwt',
        'jewels',
    ]

    
******************
jewels_service/jewels/serializers.py
jewels_service/jewels/urls.py
jewels_service/settings.py


jewels_service/jewels/models.py
jewels_service/jewels/serializers.py
jewels_service/jewels/urls.py
jewels_service/jewels/views.py
jewels_service/jewels_service/urls.py
************************
Hacer las migraciones
    python manage.py makemigrations
    python manage.py migrate
*********************

create a superuser
    python manage.py createsuperuser


*****************
Add JWT Settings:
Add JWT settings to jewels_service/settings.py

