from apps.core.api.v1.captcha_component import Captcha
from rest_framework import serializers

from config.settings import CAPTCHA_NUM_CARACTERS


class CaptchaSerializer(serializers.Serializer):
    class Meta:
        model = Captcha
        fields = '__all__'


class DataVerifySerializer(serializers.Serializer):
    uuid = serializers.CharField(required=True, max_length=100)
    user_input = serializers.CharField(required=True, max_length=CAPTCHA_NUM_CARACTERS)

class DataVerifyPassedSerializer(serializers.Serializer):
    uuid = serializers.CharField(required=True, max_length=100)

class DataGetCaptchaSerializer(serializers.Serializer):
    width = serializers.IntegerField(required=False, default=200, max_value=400)
    height = serializers.IntegerField(required=False, default=60, max_value=100)
    font_size = serializers.IntegerField(required=False, default=50, max_value=100)