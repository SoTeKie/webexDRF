from rest_framework import viewsets
from podnety.models import Podnet
from podnety.serializers import PodnetSerializer


class PodnetView(viewsets.ModelViewSet):
    serializer_class = PodnetSerializer
    queryset = Podnet.objects.order_by('-uploadDate')
