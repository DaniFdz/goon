import pytest
from model_bakery import baker


@pytest.fixture
def category(db):
    return baker.make("Categorie", name="Category Test", description="Test Description")
