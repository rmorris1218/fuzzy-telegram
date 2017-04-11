from main import create_app

import pytest

@pytest.fixture
def app():
    app = create_app()
    return app

# @pytest.fixture
# def app_client(app):
#     client = app.test_client()
#     return client
