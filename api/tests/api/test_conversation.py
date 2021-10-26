import pytest


@pytest.mark.django_db
def test_add_conversation(client, conversation):
    """Ensure conversation details returns 201"""
    resp = client.post(
        "/api/conversations/",
        {
            "store_id": 1,
            "operator_id": 1,
            "client_id": 1,
            "status": "RESOLVED"
        },
        content_type="application/json"
    )
    assert resp.status_code == 201


@pytest.mark.django_db
def test_add_conversation(client, conversation):
    """Ensure conversation details returns 201"""
    resp = client.post(
        "/api/conversations/",
        {
            "store_id": 1,
            "operator_id": 1,
            "client_id": 1,
            "status": "RESOLVED"
        },
        content_type="application/json"
    )
    assert resp.status_code == 201


@pytest.mark.django_db
def test_add_conversation_invalid_json(client, conversation):
    """Test if an empty json is sent"""
    resp = client.post(
        "/api/conversations/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400


@pytest.mark.django_db
def test_add_conversation_invalid_json_keys(client, conversation):
    """Return 400 if the keys are not correct"""
    resp = client.post(
        "/api/conversations/",
        {
            "operator_id": 1,
            "client_id": 1,
        },
        content_type="application/json"
    )
    assert resp.status_code == 400


@pytest.mark.django_db
def test_get_single_conversation(client, conversation):
    """Return 200 if fetching a conversation is sucessful"""
    resp = client.get(f"/api/conversations/{conversation.id}/")
    assert resp.status_code == 200


@pytest.mark.django_db
def test_get_single_conversation_incorrect_id(client, conversation):
    """Return 404 if an incorrect id is provided"""
    resp = client.get("/api/conversations/incorrectid/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_conversations(client, conversation_in_bulk):
    """Return 200 when getting all conversations"""
    assert len(conversation_in_bulk) == 10
    resp = client.get("/api/conversations/")
    assert resp.status_code == 200


@pytest.mark.django_db
def test_remove_conversations(client, conversation):
    """Test to ensure that a conversation has been removed"""
    resp = client.get(f"/api/conversations/{conversation.id}/")
    assert resp.status_code == 200

    resp_two = client.delete(f"/api/conversations/{conversation.id}/")
    assert resp_two.status_code == 204

    resp_three = client.get("/api/conversations/")
    assert resp_three.status_code == 200
    assert len(resp_three.data) == 0


@pytest.mark.django_db
def test_remove_conversation_incorrect_id(client, conversation):
    """Return 404 if the id is incorrect"""
    resp = client.delete('/api/conversations/99/')
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_conversation_incorrect_id(client, conversation):
    """Return 404 if id is incorrect when updating a conversation"""
    resp = client.put('/api/conversations/99/')
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_conversation_invalid_json(client, conversation):
    """Return 404 if json is empty incorrect when a updating conversation"""
    resp = client.put(
        f'/api/conversations/{conversation.id}/',
        {},
        content_type="application/json")
    assert resp.status_code == 400


@pytest.mark.django_db
def test_update_conversation_invalid_json_keys(client, conversation):
    """Return 404 if id json keys are incomplete or incorrect when updating conversation"""
    resp = client.put(
        f'/api/conversations/{conversation.id}/',
        {"status": "error"},
        content_type="application/json")
    assert resp.status_code == 400
