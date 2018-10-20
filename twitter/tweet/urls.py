from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^homepage/$', views.HomepageApi.as_view(), name='homepage'),
    url(r'^tweet/$', views.TweetApi.as_view(), name='tweet'),
    url(r'^tweets/(?P<pk>[0-9]+)/$', views.TweetDetailApi.as_view(), name='tweet-detail'),
    url(r'^mytweets/$', views.MyTweetsApi.as_view(), name='mytweets'),
]