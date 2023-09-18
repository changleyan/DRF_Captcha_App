from django.utils import timezone

from django.shortcuts import get_object_or_404

from apps.core.api.v1.captcha_component import Captcha
from common.utils.utils import get_uuid
from rest_framework import exceptions


def saveDataCaptcha(image_text: str, app: int):
    uuid = get_uuid()
    captcha_obj = Captcha(
        uuid=uuid,
        captcha_text=image_text,
        application_id=app)
    try:
        captcha_obj.save()
    except Exception as ex:
        raise exceptions.APIException(detail=ex)
    return uuid

def getCaptchaByUuid(uuid):
    captcha_obj = get_object_or_404(Captcha, uuid=uuid)
    return captcha_obj

def setCaptchaActive(captcha_obj):
    captcha_obj.active = False
    captcha_obj.save()

def captchaIsExpired(captcha_obj):
    expired = captcha_obj.expiration_date < timezone.now()
    if expired:
        setCaptchaActive(captcha_obj)
    return expired

def captchaIsActive(captcha_obj):
    return captcha_obj.active

def captchaIsPaset(captcha_obj):
    passed_captcha = captcha_obj.pass_captcha
    if passed_captcha:
        setCaptchaActive(captcha_obj)
    return captcha_obj.pass_captcha
def captchaIsValid(captcha_obj):
    return False if(captchaIsPaset(captcha_obj) or not captchaIsActive(captcha_obj)) else True

def setCaptchaPaset(captcha_obj):
    captcha_obj.pass_captcha = True
    captcha_obj.save()

def validateTextCaptcha(captcha_obj, input_text_user):
    isValid = str(captcha_obj.captcha_text).lower() == str(input_text_user).lower()
    # Seteo el parametro pass_captcha a True
    setCaptchaPaset(captcha_obj)
    return isValid

def verifyCaptchaIsValidated(captcha_obj):
    passed_captcha = captcha_obj.pass_captcha
    isActive = captcha_obj.active
    if isActive:
        setCaptchaActive(captcha_obj)
    return passed_captcha and isActive