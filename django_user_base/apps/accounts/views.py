from django.shortcuts import render

from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class MeView(generics.RetrieveAPIView):
    """
    GET /api/accounts/me/
    Returns the authenticated User and related Profile.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self): # type:ignore
        return self.request.user


from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


from django.views.generic import TemplateView

class LoginPageView(TemplateView):
    template_name = "accounts/login.html"
