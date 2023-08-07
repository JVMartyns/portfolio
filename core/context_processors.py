from django.conf import settings
from django.utils import translation


def languages(request):
    current_language = translation.get_language()
    languages = settings.LANGUAGES

    for i, (code, _name) in enumerate(languages):
        if code == current_language:
            languages.insert(0, languages.pop(i))
            break

    context = {'languages': languages, }

    return context


def themes(request):
    current_theme = request.COOKIES.get('django_theme', settings.DEFAULT_THEME)
    themes = settings.THEMES

    for i, (code, _name) in enumerate(themes):
        if code == current_theme:
            themes.insert(0, themes.pop(i))
            break

    context = {'themes': themes, 'theme': current_theme, }

    return context


def google_analytics(request):
    context = {}
    if hasattr(settings, 'GA_TRACKING_ID') and settings.GA_TRACKING_ID:
        return {'GA_TRACKING_ID': settings.GA_TRACKING_ID}
    return context
