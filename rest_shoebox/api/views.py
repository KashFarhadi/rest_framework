from rest_framework.viewsets import ModelViewSet
from .serializers import ManufacturerSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer
from ..models import Manufacturer, ShoeType, ShoeColor, Shoe

class ManufacturerViewSet(ModelViewSet):
    """
    API endpoint that allows Manufacturers to be viewed or edited.
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class ShoeTypeViewSet(ModelViewSet):
    """
    API endpoint that allows Shoe Type to be viewed or edited.
    """
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer

class ShoeColorViewSet(ModelViewSet):
    """
    API endpoint that allows Shoe Color to be viewed or edited.
    """
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer

class ShoeViewSet(ModelViewSet):
    """
    API endpoint that allows Shoes to be viewed or edited.
    """
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
