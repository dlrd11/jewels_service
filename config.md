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