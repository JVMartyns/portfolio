from django.conf import settings
from django.utils import translation


def languages(request):
    current_language = translation.get_language()
    languages = settings.LANGUAGES
    return {'languages': languages, "current_language": current_language}


def themes(request):
    current_theme = request.COOKIES.get(
        'current_theme', settings.DEFAULT_THEME
    )
    themes = settings.THEMES
    return {'themes': themes, 'current_theme': current_theme}


def google_analytics(request):
    context = {}
    if hasattr(settings, 'GA_TRACKING_ID') and settings.GA_TRACKING_ID:
        return {'GA_TRACKING_ID': settings.GA_TRACKING_ID}
    return context
