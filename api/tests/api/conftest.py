import pytest
from model_bakery import baker

from api.models import Conversation


@pytest.fixture()
def conversation():
    """Fixture to help create data for the Conversation model."""
    return baker.make(Conversation)


@pytest.fixture()
def conversation_in_bulk():
    """Fixture to help create bulk data for the Conversation model."""
    return baker.make(Conversation, _quantity=10)
