from datetime import timedelta

import requests
from django.utils import timezone

last_updated = timezone.now() - timedelta(minutes=10)
cached_inventory_dict = None

def load_inventory():
    global last_updated
    global cached_inventory_dict

    if last_updated + timedelta(minutes=5) < timezone.now():
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
        cached_inventory_dict = inventory_dict
        last_updated = timezone.now()
    return cached_inventory_dict
