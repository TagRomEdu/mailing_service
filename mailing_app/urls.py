from django.urls import path

from mailing_app.apps import MailingAppConfig
from mailing_app.views import contact, index, BlogListView, MailingListView, BlogDetailView, \
    MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView

app_name = MailingAppConfig.name
urlpatterns = [
    path('', index, name='index'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<slug>', BlogDetailView.as_view(), name='blog_single'),
    path('mailing_create/', MailingCreateView.as_view(), name='create_mailing'),
    path('mailing_update/<int:pk>', MailingUpdateView.as_view(), name='update_mailing'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>', MailingDetailView.as_view(), name='mailing_single'),
    path('mailing/<int:pk>/confirm_delete', MailingDeleteView.as_view(), name='delete_mailing'),
    path('contact/', contact, name='contact'),
]
