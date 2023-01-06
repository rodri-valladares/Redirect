from django.urls import path
from .views import get_url_redirect

urlpatterns = [
    path(r'redirect/<str:key>',get_url_redirect,name='redirect')
]