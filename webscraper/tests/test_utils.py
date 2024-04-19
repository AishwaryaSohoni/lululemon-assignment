from unittest import mock

import utils
from utils import load_inventory

sample_http_response = {
    "contents": [{"mainContent": [{"contents": [{"records": [{"attributes": {"product.defaultSku": ["sku1"], "product.displayName": ["Lulu stretchy leggings"], "product.activity": ["Yoga"], "product.price": ["100"]}}]}]}]}]}


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

@mock.patch("requests.get", return_value=MockResponse(sample_http_response, 200))
def test_load_inventory(mock_requests_get):
    expected_result = {"sku1": {"display_name": "Lulu stretchy leggings", "product_activity": ["Yoga"], "product_price": "100"}}

    response = load_inventory()

    assert response == expected_result


@mock.patch("requests.get")
def test_load_inventory__fetches_cached_value_when_recently_updated(mock_requests_get):
    utils.last_updated = utils.timezone.now()
    utils.cached_inventory_dict = {"cached": "value"}

    response = load_inventory()

    assert response == utils.cached_inventory_dict
    mock_requests_get.assert_not_called()

