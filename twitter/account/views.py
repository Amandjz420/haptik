# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from elapi import CreateView, RetrieveView, UpdateView, DeleteView
from .schema import PeopleSchema, LoginSchema, LogoutSchema, ProfileSelectionApiSchema
from .models import People


class SignUp(CreateView):

    schema_class = PeopleSchema
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


class ProfileSelectionApi(RetrieveView, UpdateView, DeleteView):

    schema_class = ProfileSelectionApiSchema

    def get_queryset(self):
        return People.objects.all()

    def get_schema_kwargs(self):
        kwargs = super(ProfileSelectionApi, self).get_schema_kwargs()
        kwargs['context'].update({
            'method': self.request.method
        })
        if self.request.method == 'DELETE':
            kwargs.update({'partial': True})
        return kwargs

    def perform_update(self, instance, data):
        increase_follow = data.pop('increase_follow', False)
        follower_change = data.pop('follower_change', False)
        for key, value in data.iteritems():
            if key == 'followed':
                if increase_follow & follower_change:
                    value += instance.followed
                    value = list(set(value))
                elif follower_change:
                    value = list(set(instance.followed) - set(value))
            setattr(instance, key, value)
        instance.save()
        return ProfileSelectionApiSchema().dump(instance).data

    def perform_delete(self, instance, data):
        instance.delete()
        return {"status": "Deleted"}

