from rest_framework import viewsets

from .models import ReformaItem
from .serializers import ReformaItemSerializer


class ReformaItemViewSet(viewsets.ModelViewSet):
    queryset = ReformaItem.objects.all()
    serializer_class = ReformaItemSerializer
