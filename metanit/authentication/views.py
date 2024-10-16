from django.shortcuts import render

# Create your views here.
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.yandex.views import YandexAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

class YandexLogin(SocialLoginView):
  adapter_class = YandexAuth2Adapter
  callback_url = "http://127.0.0.1:8000/"
  client_class = OAuth2Client