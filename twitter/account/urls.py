from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.SignUp.as_view(), name='sign-up'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),

]