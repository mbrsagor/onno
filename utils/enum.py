from enum import Enum


class UserRole(Enum):
    CONSUMER = 1
    MERCHANT = 2

    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]


# Add role permission
allow_access_consumer = UserRole.CONSUMER.value
allow_access_merchant = UserRole.MERCHANT.value


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

    @classmethod
    def get_gender(cls):
        return [(key.value, key.name) for key in cls]


class STATUS(Enum):
    PENDING = 1
    ACCEPTED = 2
    DECLINE = 3

    @classmethod
    def get_status(cls):
        return [(key.value, key.name) for key in cls]
