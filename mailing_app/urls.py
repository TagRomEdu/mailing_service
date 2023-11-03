from django.urls import path

from mailing_app.apps import MailingAppConfig
from mailing_app.views import blog_single, browsejobs, contact, index, BlogListView

app_name = MailingAppConfig.name
urlpatterns = [
    path('', index, name='index'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog_single/', blog_single, name='blog_single'),
    path('browsejobs/', browsejobs, name='browsejobs'),
    path('contact/', contact, name='contact'),
]
