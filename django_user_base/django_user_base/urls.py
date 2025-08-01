from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # dj-rest-auth: login/logout/password reset/etc
    path("api/auth/", include("dj_rest_auth.urls")),
    # auth adapters
    path("api/auth/", include("apps.accounts.urls")),

    # account pages
    path("accounts/", include("apps.accounts.urls")),

    # dj-rest-auth registration (signup + email confirmation)
    path("api/auth/registration/", include("dj_rest_auth.registration.urls")),

    # dj-rest-auth social login (Google, Facebook, etc)
    # this module is provided by dj-rest-auth[with_social]
    # path("api/auth/social/", include("dj_rest_auth.social_urls")), -> recommended but having trouble, should fix

    # alternative social auth
    path("api/auth/social/", include("allauth.socialaccount.urls")),
    path("accounts/", include("allauth.urls")),

    # Your “accounts” app: profile + any custom endpoints
    path("api/accounts/", include("apps.accounts.urls")),

    # OpenAPI schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    # Swagger UI
    path(
        "api/docs/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),

    # Redoc UI
    path(
        "api/docs/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]