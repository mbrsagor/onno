from django.db import models
from django.utils.translation import gettext_lazy as _
from enum import IntEnum


class BrandGroup(models.TextChoices):
    NOBRAND = 'NOBRAND', _('NO BRAND')
    BRAND1 = 'BRAND1', _('Brand 1')
    BRAND2 = 'BRAND2', _('2-5 Brand')
    BRAND3 = 'BRAND3', _('6-10 Brand')
    BRAND4 = 'BRAND4', _('10+ Brand')


class PaymentMethod(models.TextChoices):
    CARD = 'CARD', _('Card')
    CASH = 'CASH', _('Cash')


class AddressType(models.TextChoices):
    BILLING = 'BILLING', _('Billing')
    SHIPPING = 'SHIPPING', _('Shipping')


class STATUS(IntEnum):
    ALL = 0
    NEW = 1
    KITCHEN = 2
    READY = 3

    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]


class InventoryType(models.TextChoices):
    ITEM = 'ITEM', _('Item')
    MODIFIER = 'MODIFIER', _('Modifier')


class ModifierType(models.TextChoices):
    SINGLE = 'SINGLE', _('Single')
    Multiple = 'Multiple', _('MULTIPLE')


class PlatformChoice(models.TextChoices):
    ONNO = 'ONNO', _('Onno')
