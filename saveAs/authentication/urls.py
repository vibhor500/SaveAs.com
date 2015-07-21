from django.conf.urls import include, url
from apis import remote_authentication

urlpatterns = [
    url(r'^google_auth', remote_authentication.google_authentication),
    url(r'^oauth2callback', remote_authentication.abc),
]

