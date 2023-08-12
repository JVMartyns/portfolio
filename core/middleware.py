from django.core.cache import cache
from core import models


class SocialLinksMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        social_links = cache.get('social_links')

        if not social_links:
            social_links = models.SocialLink.objects.all()
            cache.set('social_links', social_links)

        request.social_links = social_links
        response = self.get_response(request)

        return response
