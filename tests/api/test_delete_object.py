def test_delete_object(playwright):
    request = playwright.request.new_context()
    response = request.delete("https://api.restful-api.dev/objects/6")
    
    json_data = response.json()
    print("response : ",json_data)
    
    assert response.status == 405
    
    print("test passed....")
    request.dispose()