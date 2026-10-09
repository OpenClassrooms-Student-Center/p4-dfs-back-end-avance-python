from rest_framework import viewsets

from .models import Demande
from .serializers import DemandeSerializer


class DemandeViewSet(viewsets.ModelViewSet):
    queryset = Demande.objects.all().order_by("id")
    serializer_class = DemandeSerializer
    http_method_names = ["get", "post", "put"]