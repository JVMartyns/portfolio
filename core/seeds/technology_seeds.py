from django.core.files import File
from core.models import Technology

technologies = {
    'Elixir': 'media_aux/technologies/elixir.svg',
    'Phoenix': 'media_aux/technologies/phoenix.svg',
    'Python': 'media_aux/technologies/python.svg',
    'Django': 'media_aux/technologies/django-plain.svg',
    'HTML': 'media_aux/technologies/html5.svg',
    'CSS': 'media_aux/technologies/css3.svg',
    'JavaScript': 'media_aux/technologies/javascript.svg',
    'PostgreSQL': 'media_aux/technologies/postgresql.svg',
    'SQLite': 'media_aux/technologies/sqlite.svg',
    'Git': 'media_aux/technologies/git.svg',
    'GitHub': 'media_aux/technologies/github.svg',
    'Docker': 'media_aux/technologies/docker.svg',
    'Jenkins': 'media_aux/technologies/jenkins.svg',
    'Jira': 'media_aux/technologies/jira.svg',
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
