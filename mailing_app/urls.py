from django.urls import path

from mailing_app.apps import MailingAppConfig
from mailing_app.views import homepage

app_name = MailingAppConfig.name
urlpatterns = [
    path('', homepage),
]
