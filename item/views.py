from rest_framework.permissions import AllowAny
from rest_framework import generics

from .models import Mobile, HandsFree
from .serializers import MobileSerializer, HandsFreeSerializer
from drf_multiple_model.views import ObjectMultipleModelAPIView


class ItemAPIView(ObjectMultipleModelAPIView):
    permission_classes = (AllowAny,)
    querylist = [
        {'queryset': Mobile.objects.all(), 'serializer_class': MobileSerializer},
        {'queryset': HandsFree.objects.all(), 'serializer_class': HandsFreeSerializer},
    ]


class CreateMobileView(generics.CreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
