from app.api.serializers import PersonSerializer
from app.models import Person
from rest_framework.generics import ListAPIView


class PersonAPIView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
