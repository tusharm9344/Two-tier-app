import pytest
import os
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'

from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_index(client):
    res = client.get('/')
    assert res.status_code == 200

def test_add_note(client):
    res = client.post('/notes', data={'content': 'test note'})
    assert res.status_code == 204
