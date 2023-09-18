from django.urls import path, include
from rest_framework import routers

from apps.core.api.v1.captcha_component import CaptchaViewSet
from apps.core.api.v1.group_component import GroupViewSet
from apps.core.api.v1.user_component import UserViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'captcha', CaptchaViewSet)


urlpatterns = [
    path('', include(router.urls), ),
]
