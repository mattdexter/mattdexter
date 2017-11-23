from django.views import generic
from rest_framework_mongoengine import viewsets
from .serializers import *
from .models import *


class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects