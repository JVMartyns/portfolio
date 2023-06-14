from django.conf import settings
from django.utils import translation


def languages(request):
    current_language = translation.get_language()
    languages = settings.LANGUAGES

    for i, (code, _name) in enumerate(languages):
        if code == current_language:
            languages.insert(0, languages.pop(i))
            break

    return {
        'languages': settings.LANGUAGES,
    }


def themes(request):
    current_theme = request.COOKIES.get('django_theme', settings.DEFAULT_THEME)
    themes = settings.THEMES

    for i, (code, _name) in enumerate(themes):
        if code == current_theme:
            themes.insert(0, themes.pop(i))
            break

    print(current_theme)
    return {
        'themes': themes,
        'current_theme': current_theme,
    }
