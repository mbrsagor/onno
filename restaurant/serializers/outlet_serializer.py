from rest_framework import serializers
from restaurant.models.outlets import Day, OrderDelivery, OrderPickUp, Outlet
from restaurant.serializers.order_item_serializer import OrderSerializer


class OutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = (
            'id', 'restaurant', 'name', 'address', 'area', 'phone', 'email', 'is_publish', 'is_shared', 'avatar',
            'tax_rate', 'same_day', 'next_day'
        )
        read_only_fields = ['restaurant']


class OrderDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDelivery
        fields = (
            'id', 'outlet', 'is_open', 'payment_method', 'preparation', 'preparation_delivery', 'delivery_free',
            'min_order_value', 'area_file'
        )
        read_only_fields = ['outlet']


class OrderPickUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPickUp
        fields = (
            'id', 'outlet', 'is_open', 'payment_method', 'preparation'
        )
        read_only_fields = ['outlet']


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'


class OrderOutletGraphSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()

    class Meta:
        model = Outlet
        fields = [
            'id', 'orders'
        ]

    def get_orders(self, obj):
        return OrderSerializer(obj.order_outlet.all(), many=True).data
