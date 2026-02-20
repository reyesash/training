def test_root_redirect(client):
    # Arrange: client fixture provided
    # Act: request root without following redirects
    resp = client.get("/", follow_redirects=False)

    # Assert: should redirect to static index
    assert resp.status_code in (302, 307)
    assert resp.headers["location"] == "/static/index.html"
