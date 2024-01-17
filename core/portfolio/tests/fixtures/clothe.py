import pytest
from model_bakery import baker


@pytest.fixture
def clothe(category, db):
    return baker.make(
        "Clothe",
        name="Clothe Test",
        description="Clothe Test Description",
        category=category,
    )


@pytest.fixture
def clothe_no_category(db):
    return baker.make("Clothe", name="Clothe Test", description="Clothe Test Description")
