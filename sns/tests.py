from django.test import TestCase
import pytest
from django.test import Client

# Create your tests here.

@pytest.mark.django_db
def test_views_search():
    c = Client()
    response = c.get('/login/')
    assert response.status_code == 200
    response = c.get('/logout/')
    assert response.status_code == 302
    response = c.get('/register/')
    assert response.status_code == 200
    response = c.get('/wall/')
    assert response.status_code == 302
    response = c.get('/settings/profile/')
    assert response.status_code == 302
    response = c.get('/settings/edit/')
    assert response.status_code == 302
    response = c.get('/settings/pw/')

