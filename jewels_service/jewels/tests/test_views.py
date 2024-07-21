import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from unittest.mock import patch


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_jewel(db):
    from jewels.models import Jewel
    return Jewel.objects.create(
        name="Test Jewel",
        description="A test jewel",
        price=100.00
    )


@patch('jewels.utils.verify_token')
def test_list_jewels_with_valid_token(mock_verify_token, api_client, create_jewel):
    mock_verify_token.return_value = True  # Simulate valid token
    url = reverse('jewel-list-create')
    response = api_client.get(url, HTTP_AUTHORIZATION='Bearer valid_token')

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == create_jewel.name


@patch('jewels.utils.verify_token')
def test_list_jewels_without_token(mock_verify_token, api_client, create_jewel):
    mock_verify_token.return_value = False  # Simulate no token
    url = reverse('jewel-list-create')
    response = api_client.get(url)

    assert response.status_code == 200  # Should be allowed as token is optional
    assert len(response.data) == 1
    assert response.data[0]['name'] == create_jewel.name


@patch('jewels.utils.verify_token')
def test_create_jewel_with_valid_token(mock_verify_token, api_client):
    mock_verify_token.return_value = True  # Simulate valid token
    url = reverse('jewel-list-create')
    data = {
        "name": "New Jewel",
        "description": "A new test jewel",
        "price": 200.00
    }
    response = api_client.post(url, data, format='json', HTTP_AUTHORIZATION='Bearer valid_token')

    assert response.status_code == 201
    assert response.data['name'] == data['name']


@patch('jewels.utils.verify_token')
def test_create_jewel_without_token(mock_verify_token, api_client):
    mock_verify_token.return_value = False  # Simulate no token
    url = reverse('jewel-list-create')
    data = {
        "name": "New Jewel",
        "description": "A new test jewel",
        "price": 200.00
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == 401  # Should be unauthorized
