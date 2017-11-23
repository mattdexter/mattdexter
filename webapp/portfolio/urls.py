from django.conf.urls import url, include
from rest_framework import routers
from . import views

app_name = 'portfolio'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, base_name="User")

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^api/portfolio/', include(router.urls)),
]