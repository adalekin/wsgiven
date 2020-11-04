def test_basic_not_found(fx_http_client):
    response = fx_http_client.request(method="GET", path="/")
    assert response.status == 404
