from django.urls import path
from django.views.decorators.cache import cache_page

from mailing_app.apps import MailingAppConfig
from mailing_app.views import contact, index, BlogListView, MailingListView, BlogDetailView, \
    MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, BlogDeleteView, BlogCreateView, \
    BlogUpdateView, MailingUpdateStatusView, ClientCreateView, ClientUpdateView, ClientDetailView, ClientDeleteView, \
    ClientListView

app_name = MailingAppConfig.name
urlpatterns = [
    path('', index, name='index'),
    path('blog_create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog_update/<slug>', BlogUpdateView.as_view(), name='update_blog'),
    path('blog/', cache_page(60)(BlogListView.as_view()), name='blog_list'),
    path('blog/<slug>', BlogDetailView.as_view(), name='blog_single'),
    path('blog/<slug>/confirm_delete', BlogDeleteView.as_view(), name='delete_blog'),
    path('mailing_create/', MailingCreateView.as_view(), name='create_mailing'),
    path('mailing_update/<int:pk>', MailingUpdateView.as_view(), name='update_mailing'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>', MailingDetailView.as_view(), name='mailing_single'),
    path('mailing/<int:pk>/confirm_delete', MailingDeleteView.as_view(), name='delete_mailing'),
    path('contact/', contact, name='contact'),
    path('change_status/<int:pk>', MailingUpdateStatusView.as_view(), name='change_status'),
    path('client_create/', ClientCreateView.as_view(), name='create_client'),
    path('client_update/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='client_single'),
    path('client/<int:pk>/confirm_delete', ClientDeleteView.as_view(), name='delete_client'),
]
