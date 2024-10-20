from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CacheViewMixin:
    cache_timeout = settings.CACHE_TIME_SHORT

    @method_decorator(cache_page(cache_timeout))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
