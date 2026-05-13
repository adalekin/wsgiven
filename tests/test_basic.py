def test_basic_not_found(fx_http_client):
    response = fx_http_client.get("/")
    assert response.status_code == 404
