from nturl2path import url2pathname
from django.urls import path
from .views import signupview

urlpatterns=[
    path('signup/',signupview.as_view(),name='signup')
]