import requests
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response


def load_inventory():
    response = requests.get('https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json')
    inventory = response.json()["contents"][0]["mainContent"][0]["contents"][0]["records"]
    print(":::: Inventory count ::::: ", len(inventory))

    inventory_dict = {}
    for item in inventory:
        sku = item["attributes"]["product.defaultSku"][0]
        display_name = item["attributes"]["product.displayName"][0]
        product_activity = item["attributes"]["product.activity"]
        product_price = item["attributes"]["product.price"][0]
        inventory_dict[sku] = {"display_name": display_name, "product_activity": product_activity,
                               "product_price": product_price}

    print(":::: Inventory dict ::::: ", inventory_dict)
    return inventory_dict

class WomensLeggingsInfoView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        inventory_response = load_inventory()
        return Response(inventory_response, status=status.HTTP_200_OK)
