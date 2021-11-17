from django.contrib import admin

from restaurant.models.outlets import (
    Outlet,
    OrderDelivery,
    OrderPickUp,
    Day
)
from restaurant.models.restaurants import Restaurant, RestaurantUser
from restaurant.models.inventory import (
    Inventory,
    Menus,
    Category,
    Modifier
)
from restaurant.models.location import Location
from restaurant.models.order_items import (
    OrderItem,
    Order,
    Payment,
    Address,
    Coupon
)
from restaurant.models.application import ApplicationSetting

admin.site.register(Outlet)
admin.site.register(OrderDelivery)
admin.site.register(OrderPickUp)
admin.site.register(Day)
admin.site.register(Restaurant)
admin.site.register(RestaurantUser)
admin.site.register(Inventory)
admin.site.register(Menus)
admin.site.register(Category)
admin.site.register(Modifier)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Address)
admin.site.register(Coupon)
admin.site.register(Location)
admin.site.register(ApplicationSetting)
