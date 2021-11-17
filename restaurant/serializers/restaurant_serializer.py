from accounts.serializers import UserSerializer
from rest_framework import serializers
from restaurant.models.order_items import Order
from restaurant.models.restaurants import Restaurant, RestaurantUser


class RestaurantUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = RestaurantUser
        fields = (
            'id', 'name', 'is_owner', 'email'
        )

    def get_name(self, obj):
        return obj.user.first_name + " " + obj.user.last_name

    def get_is_owner(self, obj):
        return obj.user.is_owner

    def get_email(self, obj):
        return obj.user.email


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            'id', 'name', 'owner', 'sub_domain', 'avatar'
        )
        read_only_fields = ['owner']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['owner'] = UserSerializer(instance.owner).data
        return response


class RestaurantOrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'order']
