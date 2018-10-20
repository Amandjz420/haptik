# from django.contrib.auth import get_user_model
# from django.db.models import Q
# from django.contrib.auth import authenticate

from account.models import People
from elapi import base_schema, fields, exceptions
from marshmallow import validates_schema, post_dump, pre_load, post_load, pre_dump


class TweetSchema(base_schema.Schema):

    id = fields.Integer(required=False)
    title = fields.String(required=False)  # validators should be a list
    msg = fields.String(required=False)
    like = fields.Integer(required=False)
    people_id = fields.Integer(required=True)

    @pre_load
    def check_msg(self, data):
        if 'msg' not in data and self.context['method'] == 'POST':
            raise exceptions.WrongDataException("tweet content is missing")
        if 'msg' in data and len(data['msg']) > 140:
            raise exceptions.WrongDataException("tweet is exceeding 140 characters.")
        if not People.objects.filter(id=data['people_id']).exists():
            raise exceptions.DataNotFoundException("No such user exists")
        return data
