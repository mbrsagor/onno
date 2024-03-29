from rest_framework import serializers
from restaurant.models.order_items import (Address, Coupon, Order, OrderItem,
                                           Payment)
from restaurant.serializers.inventory_serializer import InventorySerializer
from accounts.serializers import UserSerializer


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = (
            'id',
            'code',
            'amount'
        )


class OrderItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'item',
            'quantity',
            'final_price'
        )

    def get_item(self, obj):
        return InventorySerializer(obj.item).data

    def get_final_price(self, obj):
        return obj.get_final_price()


class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    coupon = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id', 'order_items', 'total', 'coupon', 'outlet', 'user', 'ref_code', 'items', 'start_date',
            'ordered_date', 'ordered', 'status', 'order_date', 'order_time'
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        return response

    def get_order_items(self, obj):
        return OrderItemSerializer(obj.items.all(), many=True).data

    def get_total(self, obj):
        return obj.get_total()

    def get_coupon(self, obj):
        if obj.coupon is not None:
            return CouponSerializer(obj.coupon).data
        return None


class LiveOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id', 'items', 'user', 'outlet', 'status'
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        return response


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'user',
            'street_address',
            'apartment_address',
            'zip',
            'address_type',
            'default'
        )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'id',
            'amount',
            'timestamp'
        )
