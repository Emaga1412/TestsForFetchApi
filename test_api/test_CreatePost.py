import requests
import test_data


def test_post_create():
    response = requests.post(test_data.my_url_for_create, json=test_data.my_payload, headers=test_data.my_headers)
    assert response.status_code in [200, 201], f"Unexpected status code: {response.status_code}"

    response_json = response.json()
    assert "userId" in response_json, "Key 'userId' not found in response"
    assert "id" in response_json, "Key 'id' not found in response"
    assert "title" in response_json, "Key 'title' not found in response"
    assert "body" in response_json, "Key 'body' not found in response"
