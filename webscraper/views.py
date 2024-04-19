from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from utils import load_inventory


class WomensLeggingsInfoView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        inventory_response = load_inventory()
        return Response(inventory_response, status=status.HTTP_200_OK)
