from base.models.branding import Branding
from rest_framework.serializers import ModelSerializer


class BrandingSerializer(ModelSerializer):
    class Meta:
        model = Branding
        fields = [
            'id', 'outlet', 'title', 'message', 'cover_photo', 'favicon'
        ]
        read_only_fields = ['outlet']
