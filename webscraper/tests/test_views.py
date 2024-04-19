from unittest import mock

from django.urls import reverse
from rest_framework.test import APIClient


@mock.patch("views.load_inventory", return_value={"sku1": {"display_name": "Lulu stretchy leggings", "product_activity": ["Yoga"], "product_price": "100"}})
def test_womens_leggings_info_view(mock_load_inventory):
    client = APIClient()
    #TODO : Investigate why I see the issue "apps not ready", likely a configuration issue
    url = reverse("available-womens-leggings")
    client.force_authenticate(user=mock.MagicMock())
    response = client.get("/webscraper/")

    assert response.status_code == 200
    assert response.data == {"sku1": {"display_name": "Lulu stretchy leggings", "product_activity": ["Yoga"], "product_price": "100"}}