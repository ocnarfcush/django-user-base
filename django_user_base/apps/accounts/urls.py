from django.urls import path
from .views import MeView, GoogleLogin, FacebookLogin, LoginPageView

urlpatterns = [
    # GET /api/accounts/me/ → return request.user + profile
    path("me/", MeView.as_view(), name="user-me"),
    path("social/google/",  GoogleLogin.as_view(),    name="google_login"),
    path("social/facebook/", FacebookLogin.as_view(), name="facebook_login"),
    path("login/", LoginPageView.as_view(), name="login_page"),
]