

def test_get_objects(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
        "Acccept": "application/json"
        # "Authorization":"Access Bearer token"
        }
    )
    response = request.get("https://api.restful-api.dev/objects/2")
    
    json_data = response.json()
    print("response generated : ",json_data)
    assert response.status == 200
    assert json_data["id"] == "2"
    assert json_data["data"] == None
    
    request.dispose()
    print("test passed.....")
    # assert response.headers["content-type"] == "application/json;charset==utf-8"