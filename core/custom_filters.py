from django import template
from django.utils.translation import gettext
import markdown2

register = template.Library()


@register.filter
def markdown(value: str) -> str:
    """
    This function takes in a string `value` and returns a markdown formatted string. It is a Django template filter,
    and is registered with `@register.filter`. The function uses the `markdown2` library to convert the input string 
    to markdown format, and returns the result. 

    Parameters:
    value (str): The string to be converted to markdown format.

    Returns:
    str: The input string converted to markdown format.
    """
    return markdown2.markdown(value)


@register.filter
def trans(value: str) -> str:
    """
    This function is a Django template filter that translates a given string.
    :param value: The string that needs to be translated.
    :return: The translated string.
    """
    if value == 'Graduation':
        print(gettext(value))

    return gettext(value)
