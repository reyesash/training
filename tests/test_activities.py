def test_get_activities(client):
    # Arrange: client fixture
    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_and_duplicate(client):
    activity = "Chess Club"
    email = "newstudent@example.com"

    # Arrange: ensure email not present
    assert email not in client.get("/activities").json()[activity]["participants"]

    # Act: signup
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert: success
    assert resp.status_code == 200
    assert "Signed up" in resp.json().get("message", "")

    # Act: duplicate signup
    resp2 = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert: duplicate rejected
    assert resp2.status_code == 400


def test_unregister_and_not_registered(client):
    activity = "Chess Club"
    email = "toremove@example.com"

    # Act: signup then unregister
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 200

    resp2 = client.post(f"/activities/{activity}/unregister", params={"email": email})
    assert resp2.status_code == 200

    # Act: unregister again -> should be 400
    resp3 = client.post(f"/activities/{activity}/unregister", params={"email": email})
    assert resp3.status_code == 400
