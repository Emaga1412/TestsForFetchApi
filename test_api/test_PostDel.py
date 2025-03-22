import requests
from test_api import test_data


def test_PostDel():
    response = requests.delete(url=test_data.my_url_for_changes, headers=test_data.my_headers)
    assert response.status_code in [200, 201], f"Unexpected status code: {response.status_code}"
    response_json = response.json()
    assert response_json == test_data.my_payload_delete, "post not deleted"