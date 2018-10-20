from __future__ import unicode_literals

from elapi import CreateView, RetrieveView, ListView, UpdateView, DeleteView
from .schema import TweetSchema
from account.models import People
from .models import Tweet


class TweetApi(CreateView):
    schema_class = TweetSchema

    def perform_create(self, data):
        tweet = Tweet.objects.create(**data)
        return {"id": tweet.id}


class HomepageApi(ListView):
    schema_class = TweetSchema

    def get_queryset(self):
        followed = People.objects.get(user__id=self.request.user.pk).followed
        tweets = list(Tweet.objects.filter(people__pk__in=followed).order_by('-pk'))
        return TweetSchema().dump(tweets, many=True).data


class MyTweetsApi(ListView):
    schema_class = TweetSchema

    def get_queryset(self):
        return Tweet.objects.filter(people__user__id=self.request.user.id)


class TweetDetailApi(UpdateView, DeleteView):
    schema_class = TweetSchema

    def get_schema_kwargs(self):
        kwargs = super(TweetDetailApi, self).get_schema_kwargs()
        if self.request.method == 'DELETE':
            kwargs.update({'partial': True})
        return kwargs

    def get_queryset(self):
        return Tweet.objects.all()

    def perform_update(self, instance, data):
        if instance.people.user==self.request.user:
            for key, value in data.iteritems():
                setattr(instance, key, value)
            instance.save()
            return data
        else:
            return({"Updation": "Failed because you have no rights"})

    def perform_delete(self, instance, data):
        if instance.people.user == self.request.user:
            instance.delete()
            return {"status": "Deleted"}
        else:
            return({"Deletion": "Failed because you have no rights"})
