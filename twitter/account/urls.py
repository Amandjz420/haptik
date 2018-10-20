from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^people/$', views.SignUp.as_view(), name='sign-up'),
    url(r'^people/(?P<pk>[0-9]+)/$', views.ProfileSelectionApi.as_view(), name='profile-select'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),

]