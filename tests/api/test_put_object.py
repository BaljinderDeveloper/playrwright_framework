import json
from playwright.sync_api import sync_playwright

def test_post_object():
    with sync_playwright() as p:
        request = p.request.new_context()

        response = request.post(
            "https://api.restful-api.dev/objects/7",
            data=json.dumps({
                 "name": "Apple MacBook Pro 16",
                 "data": {
                        "year": 2019,
                        "price": 2049.99,
                        "CPU model": "Intel Core i9",
                        "Hard disk size": "1 TB",
                        "color": "silver"
                         }
            }),
            headers={
                "Content-Type": "application/json"
            }
        )

        assert response.status == 400 or response.status == 405
        print(response.json())
        # print(response.body())
        # print(response.text())

        request.dispose()