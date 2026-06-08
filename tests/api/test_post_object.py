import json
from playwright.sync_api import sync_playwright

def test_post_object():
    with sync_playwright() as p:
        request = p.request.new_context()

        response = request.post(
            "https://api.restful-api.dev/objects",
            data=json.dumps({
                "name": "Apple MacBook Pro 16",
                "data": {
                    "year": 2019,
                    "price": 1849.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB"
                }
            }),
            headers={
                "Content-Type": "application/json"
            }
        )

        assert response.status == 200 or response.status == 201
        print(response.json())
        # print(response.body())
        # print(response.text())

        request.dispose()