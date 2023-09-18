from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from apps.core.api.v1.captcha_component import Captcha
from apps.core.api.v1.captcha_component.CaptchaPermissions import CaptchaAccessPolicy
from apps.core.api.v1.captcha_component.CaptchaSerializar import CaptchaSerializer, DataVerifySerializer, \
    DataVerifyPassedSerializer, DataGetCaptchaSerializer
from fast_captcha import img_captcha
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status

from apps.core.api.v1.captcha_component.CaptchaService import saveDataCaptcha, getCaptchaByUuid, captchaIsValid, \
    captchaIsExpired, validateTextCaptcha, verifyCaptchaIsValidated
from config.settings import CAPTCHA_NUM_CARACTERS


class CaptchaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Captcha.objects.all().order_by('-date')
    serializer_class = CaptchaSerializer
    permission_classes = (CaptchaAccessPolicy,)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='width',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='captcha width',
                required=False,
            ),openapi.Parameter(
                name='height',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='captcha height',
                required=False,
            ),openapi.Parameter(
                name='font_size',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='captcha font_size',
                required=False,
            )
        ]
    )
    @action(detail=False, methods=['get'])
    def get_captcha(self, request):
        serializer = DataGetCaptchaSerializer(data=request.data if len(request.data) > 0 else request.query_params)
        serializer.is_valid(raise_exception=True)

        application = request.user
        # Generar imagen
        img, text = img_captcha(
            width=serializer.data.get('width'),
            height=serializer.data.get('height'),
            font_size=serializer.data.get('font_size'),
            code_num=CAPTCHA_NUM_CARACTERS,
            img_byte='base64',
            lines_num=10)
        uuid = saveDataCaptcha(text, application.id)
        response_data = {"uuid": uuid,
                         "imagen": img}
        return Response(response_data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='uuid',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='captcha uuid',
                required=False,
            ),openapi.Parameter(
                name='user_input',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='user input',
                required=False,
            )
        ]
    )
    @action(detail=False, methods=['get'])
    def verify_captcha(self, request):
        serializer = DataVerifySerializer(data=request.data if len(request.data) > 0 else request.query_params)
        serializer.is_valid(raise_exception=True)

        uuid = serializer.data.get('uuid')
        user_input = serializer.data.get('user_input', None)

        captcha_obj = getCaptchaByUuid(uuid)
        if (captchaIsExpired(captcha_obj)):
            return Response({"msg": "Expired", "passed": False}, status=status.HTTP_400_BAD_REQUEST)

        if (captchaIsValid(captcha_obj) and validateTextCaptcha(captcha_obj, user_input)):
            return Response({"msg": "Valid", "passed": True}, status=status.HTTP_200_OK)

        return Response({"msg": "Invalid", "passed": False}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='uuid',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='captcha uuid',
                required=False,
            )
        ]
    )
    @action(detail=False, methods=['get'])
    def verify_captcha_approbed(self, request):
        serializer = DataVerifyPassedSerializer(data=request.data if len(request.data) > 0 else request.query_params)
        serializer.is_valid(raise_exception=True)

        uuid = serializer.data.get('uuid')
        captcha_obj = getCaptchaByUuid(uuid)
        if verifyCaptchaIsValidated(captcha_obj):
            return Response({"msg": "Approbed", "Valid": True}, status=status.HTTP_200_OK)
        return Response({"msg": "Not Approbed", "Valid": False}, status=status.HTTP_400_BAD_REQUEST)


