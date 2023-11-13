from django.core.cache import cache

from mailing_app.models import Client
from config import settings


def get_clients_cache():
    if settings.CACHE_ENABLED:
        key = 'client_list'
        client_list = cache.get(key)
        if client_list is None:
            client_list = Client.objects.all()
            cache.set(key, client_list)
        else:
            if client_list != Client.objects.all():
                client_list = Client.objects.all()
                cache.set(key, client_list)
    else:
        client_list = Client.objects.all()
    return client_list
