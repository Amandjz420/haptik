from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth import authenticate

from elapi import base_schema, fields, exceptions
from marshmallow import validates_schema, post_dump, pre_load, post_load

User = get_user_model()


class UserSchema(base_schema.Schema):
    username = fields.String(required=True)
    first_name = fields.String(required=False)
    last_name = fields.String(required=False)
    email = fields.String(required=True)
    password = fields.String(required=True)

    @validates_schema
    def validates_payload_data(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise exceptions.DuplicateDataException("Username already taken. Try something else")
        data['user_obj'] = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            email=data.get('email', ''),
            first_name=data.get('first_name', data['username']),
            last_name=data.get('last_name', ''))
        return data

    @post_dump
    def remove_password(self, data):
        data.pop('password', None)
        return data


class PeopleSchema(base_schema.Schema):
    id = fields.String(required=False)
    user = fields.Nested(UserSchema, attribute='user')
    phone_number = fields.String(required=False)
    birth_date = fields.Date(required=False)
    followed = fields.List(fields.Integer(), required=False)

    @pre_load
    def check_email(self, data):
        if 'email' not in data['user']:
            raise exceptions.WrongDataException("Email id is must")
        if User.objects.filter(email=data['user']['email']).exists():
            raise exceptions.DuplicateDataException("Email already taken. Try something else")
        return data

    @post_load
    def get_user(self, data):
        data['user'] = data['user']['user_obj']
        return data


class LoginSchema(base_schema.Schema):
    username_or_email = fields.String(required=True)
    password = fields.String(required=True)

    @pre_load
    def check_login_details(self, data):
        if 'username_or_email' not in data:
            raise exceptions.MissingDataException("Email or Username is required to login")
        query = Q(email=data['username_or_email'])| Q(username=data['username_or_email'])
        if not User.objects.filter(query).exists():
            raise exceptions.DataNotFoundException("Such user doesnot exist")
        else:
            username = User.objects.filter(query).first().username
            user = authenticate(username=username, password=data['password'])
            if not user:
                raise exceptions.DataNotFoundException("Invalid Credentials")
            self.user = user
        return data

    @post_load
    def get_user(self, data):
        data['user'] = self.user
        return data


class LogoutSchema(base_schema.Schema):
    username = fields.String(required=True)

    @pre_load
    def check_username(self, data):
        if not User.objects.filter(username=data['username']).exists():
            raise exceptions.DataNotFoundException("Invalid User")


class ProfileSelectionApiSchema(base_schema.Schema):
    id = fields.String(required=False)
    user_id = fields.Integer(required=False)
    phone_number = fields.String(required=False)
    followed = fields.List(fields.Integer(), required=False)
    increase_follow = fields.Boolean(required=False)
    follower_change = fields.Boolean(required=False)

