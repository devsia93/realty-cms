from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication

from realty.models import TypeRealty
from realty.serializers import TypeRealtySerializer


class TypeRealtyViewSet(ModelViewSet):
    serializer_class = TypeRealtySerializer
    queryset = TypeRealty.objects.all()
    authentication_classes = (TokenAuthentication,)
