import requests
from test_api import test_data


def test_post_change():
    response = requests.put(url=test_data.my_url_for_changes, json=test_data.my_payload_change, headers=test_data.my_headers)
    assert response.status_code in [200, 201], f"Unexpected status code: {response.status_code}"
    response_json = response.json()
    for key in test_data.my_payload_change:
        assert key in response_json

