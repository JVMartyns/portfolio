from django.core.files import File
from core.models import Technology

MEDIA_AUX = 'core/static/core/priv/media_aux/'

technologies = {
    'Elixir': MEDIA_AUX + 'technologies/elixir.svg',
    'Phoenix': MEDIA_AUX + 'technologies/phoenix.svg',
    'Python': MEDIA_AUX + 'technologies/python.svg',
    'Django': MEDIA_AUX + 'technologies/django.svg',
    'HTML': MEDIA_AUX + 'technologies/html5.svg',
    'CSS': MEDIA_AUX + 'technologies/css3.svg',
    'JavaScript': MEDIA_AUX + 'technologies/javascript.svg',
    'PostgreSQL': MEDIA_AUX + 'technologies/postgresql.svg',
    'SQLite': MEDIA_AUX + 'technologies/sqlite.svg',
    'Git': MEDIA_AUX + 'technologies/git.svg',
    'GitHub': MEDIA_AUX + 'technologies/github.svg',
    'Docker': MEDIA_AUX + 'technologies/docker.svg',
    'Jenkins': MEDIA_AUX + 'technologies/jenkins.svg',
    'Jira': MEDIA_AUX + 'technologies/jira.svg',
}


def execute_seeds():
    seeds = [
        Technology(
            name='Elixir',
            image=File(open(technologies['Elixir'], 'rb')),
            order=1
        ),
        Technology(
            name='Phoenix',
            image=File(open(technologies['Phoenix'], 'rb')),
            order=2,
        ),
        Technology(
            name='Python',
            image=File(open(technologies['Python'], 'rb')),
            order=3,
        ),
        Technology(
            name='Django',
            image=File(open(technologies['Django'], 'rb')),
            order=4,
        ),
        Technology(
            name='HTML',
            image=File(open(technologies['HTML'], 'rb')),
            order=5,
        ),
        Technology(
            name='CSS',
            image=File(open(technologies['CSS'], 'rb')),
            order=6,
        ),
        Technology(
            name='JavaScript',
            image=File(open(technologies['JavaScript'], 'rb')),
            order=7,
        ),
        Technology(
            name='PostgreSQL',
            image=File(open(technologies['PostgreSQL'], 'rb')),
            order=8,
        ),
        Technology(
            name='SQLite',
            image=File(open(technologies['SQLite'], 'rb')),
            order=9,
        ),
        Technology(
            name='Git',
            image=File(open(technologies['Git'], 'rb')),
            order=10,
        ),
        Technology(
            name='GitHub',
            image=File(open(technologies['GitHub'], 'rb')),
            order=11,
        ),
        Technology(
            name='Docker',
            image=File(open(technologies['Docker'], 'rb')),
            order=12,

        ),
        Technology(
            name='Jenkins',
            image=File(open(technologies['Jenkins'], 'rb')),
            order=13,
        ),
        Technology(
            name='Jira',
            image=File(open(technologies['Jira'], 'rb')),
            order=14,
        ),
    ]

    Technology.objects.bulk_create(seeds, ignore_conflicts=True)
