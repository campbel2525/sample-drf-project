# from django.db import transaction
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from app.core.authentications.authentications import (
    auth_model,
    create_token,
    get_user_by_token,
)
from app.core.authentications.custom_jwt_authentications import CustomJWTAuthentication

from .requests import LoginRequest, RefreshRequest, SignupRequest, UpdateRequest
from .responses import MeResponse, TokenResponse


class AccountView(viewsets.ViewSet):

    @action(
        detail=False,
        methods=["post"],
        name="accounts_login",
        authentication_classes=[],
        permission_classes=[AllowAny],
    )
    def login(self, request):
        serializer = LoginRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        auth_user = auth_model().objects.filter(email=request.data.get("email")).first()
        if auth_user is None:
            return HttpResponse("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)

        if not auth_user.check_password(request.data.get("password")):
            return HttpResponse("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)

        data = {
            "access_token": create_token(auth_user, "access_token"),
            "refresh_token": create_token(auth_user, "refresh_token"),
        }
        serializer = TokenResponse(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["get"],
        url_path="me",
        name="accounts_me",
        authentication_classes=[CustomJWTAuthentication],
        permission_classes=[AllowAny],
    )
    def me(self, request):
        serializer = MeResponse(request.user, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["post"],
        url_path="refresh",
        name="accounts_refresh",
        authentication_classes=[],
        permission_classes=[AllowAny],
    )
    def refresh(self, request):
        serializer = RefreshRequest(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"errors": serializer.errors},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        refresh_token = request.data.get("refresh_token")
        auth_user = get_user_by_token(refresh_token, "refresh_token")

        data = {
            "access_token": create_token(auth_user, "access_token"),
            "refresh_token": create_token(auth_user, "refresh_token"),
        }
        serializer = TokenResponse(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["post"],
        url_path="signup",
        name="accounts_signup",
        authentication_classes=[],
        permission_classes=[AllowAny],
    )
    def signup(self, request):
        serializer = SignupRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        auth_user = auth_model()()
        auth_user.email = request.data.get("email")
        auth_user.name = request.data.get("name")
        auth_user.password = auth_model().password_to_hash(request.data.get("password"))
        auth_user.save()

        data = {
            "access_token": create_token(auth_user, "access_token"),
            "refresh_token": create_token(auth_user, "refresh_token"),
        }
        serializer = TokenResponse(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["put"],
        url_path="update",
        name="accounts_update",
        authentication_classes=[CustomJWTAuthentication],
        permission_classes=[AllowAny],
    )
    def update_profile(self, request):
        serializer = UpdateRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        auth_user = request.user
        auth_user.email = request.data.get("email")
        auth_user.name = request.data.get("name")

        if request.data.get("password"):
            auth_user.password = auth_model().password_to_hash(
                request.data.get("password")
            )
        auth_user.save()

        serializer = MeResponse(auth_user)
        return Response(serializer.data, status=status.HTTP_200_OK)
