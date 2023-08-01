from django.core.files import File
from core.models import SocialLink

MEDIA_AUX = 'core/static/core/priv/media_aux/'


def execute_seeds():
    social_links = {
        'GitHub': MEDIA_AUX + 'social_links/github.svg',
        'LinkedIn': MEDIA_AUX + 'social_links/linkedin.svg',
        'WhatsApp': MEDIA_AUX + 'social_links/whatsapp.svg',
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
            name='WhatsApp',
            image=File(open(social_links['WhatsApp'], 'rb')),
            url='https://api.whatsapp.com/send?phone=5581982940400',
        ),
    ]

    SocialLink.objects.bulk_create(seeds, ignore_conflicts=True)
