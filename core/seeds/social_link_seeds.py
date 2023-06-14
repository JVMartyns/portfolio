from django.core.files import File
from core.models import SocialLink


def execute_seeds():
    social_links = {
        'GitHub': 'media_aux/social_links/github.svg',
        'LinkedIn': 'media_aux/social_links/linkedin.svg',
        'Instagram': 'media_aux/social_links/Instagram.svg',
    }

    seeds = [
        SocialLink(
            name='GitHub',
            image=File(open(social_links['GitHub'], 'rb')),
            url='https://github.com/JVMartyns',
        ),
        SocialLink(
            name='LinkedIn',
            image=File(open(social_links['LinkedIn'], 'rb')),
            url='https://www.linkedin.com/in/jvmartyns/',
        ),
        SocialLink(
            name='Instagram',
            image=File(open(social_links['Instagram'], 'rb')),
            url='https://www.instagram.com/jv_martyns/',
        ),
    ]

    SocialLink.objects.bulk_create(seeds, ignore_conflicts=True)
