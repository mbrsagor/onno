from rest_framework.viewsets import ModelViewSet
from base.models.branding import Branding
from base.serializers.branding_serializer import BrandingSerializer


class BrandingViewSet(ModelViewSet):
    queryset = Branding.objects.all()
    serializer_class = BrandingSerializer

    def perform_create(self, serializer):
        serializer.save(outlet_id=self.request.user.id)

    def get_queryset(self):
        if not self.request.user.is_superuser:
            branding = Branding.objects.filter(outlet_id=self.request.user.id)
        else:
            branding = Branding.objects.all()
        return branding
