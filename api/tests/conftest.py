from publisher.views import create_publication
import pytest


@pytest.fixture
def publication_create_api():
    return create_publication()


