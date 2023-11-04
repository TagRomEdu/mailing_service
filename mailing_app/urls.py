from django.urls import path

from mailing_app.apps import MailingAppConfig
from mailing_app.views import contact, BlogListView, MailingListView, BlogDetailView, \
    MailingDetailView

app_name = MailingAppConfig.name
urlpatterns = [
    path('', index, name='index'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog_single/', BlogDetailView.as_view(), name='blog_single'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('mailing_single/', MailingDetailView.as_view(), name='mailing_single'),
    path('contact/', contact, name='contact'),
]
