# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from elapi import CreateView
from .schema import SignUpSchema, LoginSchema, LogoutSchema
from .models import People


class SignUp(CreateView):

    schema_class = SignUpSchema
    permission_classes = (AllowAny,)
    post_status_code = 201

    def perform_create(self, data):
        People.objects.create(**data)
        token, _ = Token.objects.get_or_create(user=data['user'])
        return {'token': token.key}


class Login(CreateView):

    schema_class = LoginSchema
    permission_classes = (AllowAny,)
    post_status_code = 200

    def perform_create(self, data):
        token, _ = Token.objects.get_or_create(user=data['user'])
        return {'token': token.key}


class Logout(CreateView):

    schema_class = LogoutSchema
    post_status_code = 200

    def perform_create(self, data):
        Token.objects.filter(user=self.request.user).delete()
        return {'success': 'logged out'}
