from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from restaurant.models.order_items import Order
from restaurant.models.restaurants import Restaurant, RestaurantUser
from restaurant.serializers.restaurant_serializer import (
    RestaurantOrderListSerializer, RestaurantSerializer, RestaurantUserSerializer)


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RestaurantOrderList(ListAPIView):
    serializer_class = RestaurantOrderListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class RestaurantUsers(APIView):
    def get(self, *args, **kwargs):
        subdomain = self.kwargs['subdomain']
        restaurant = Restaurant.objects.get(sub_domain=subdomain)
        users = RestaurantUser.objects.filter(restaurant=restaurant)
        response = RestaurantUserSerializer(users, many=True).data
        return Response(response, status=status.HTTP_202_ACCEPTED)

