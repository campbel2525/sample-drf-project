"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.accounts.views import AccountView
from app.users.views import UserView

router = DefaultRouter()
router.register(r"api/v1/accounts", AccountView, basename="accounts")
router.register(r"api/v1/users", UserView, basename="users")


urlpatterns = [
    path("", include(router.urls)),
    path("api/hc/", include("app.hc.urls")),
]

# if settings.DEBUG:
#     urlpatterns.append(
#         path("docs/schema/", SpectacularAPIView.as_view(), name="schema"),
#     )
#     urlpatterns.append(
#         path(
#             "docs/ui/",
#             SpectacularSwaggerView.as_view(url_name="schema"),
#             name="ui",
#         ),
#     )
#     urlpatterns.append(
#         path(
#             "docs/redoc/",
#             SpectacularRedocView.as_view(url_name="schema"),
#             name="redoc",
#         ),
#     )