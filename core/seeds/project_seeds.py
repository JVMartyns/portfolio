from django.core.files import File
from django.db import IntegrityError
from core.models import Project, Technology


def execute_seeds():
    technologies = {
        'Python': Technology.objects.get(name='Python'),
        'Django': Technology.objects.get(name='Django'),
        'Elixir': Technology.objects.get(name='Elixir'),
        'Phoenix': Technology.objects.get(name='Phoenix'),
        'JavaScript': Technology.objects.get(name='JavaScript'),
        'HTML': Technology.objects.get(name='HTML'),
        'CSS': Technology.objects.get(name='CSS'),
        'PostgreSQL': Technology.objects.get(name='PostgreSQL'),
        'SQLite': Technology.objects.get(name='SQLite'),
        'Git': Technology.objects.get(name='Git'),
        'GitHub': Technology.objects.get(name='GitHub'),
        'Docker': Technology.objects.get(name='Docker'),
        'Jenkins': Technology.objects.get(name='Jenkins'),
        'Jira': Technology.objects.get(name='Jira'),
    }

    projects = {
        'Portfólio': 'media_aux/projects/portfolio_cover_image.png',
        'Desafio Bank API Cumbuca': 'media_aux/projects/bank_api_cover_image.png',
        'Desafio Codificador de Texto': 'media_aux/projects/text_encoder_challenge.png',
    }

    seeds = [
        {
            'name': 'Portfólio',
            'name_en': 'Portfolio',
            'image': File(open(projects['Portfólio'], 'rb')),
            'repository': 'https://github.com/JVMartyns/portfolio',
            'description': 'Este é o meu portfólio. Projeto feito com Django para aplicar o meu aprendizado.',
            'description_en': 'This is my portfolio. Project made with Django to apply my learning.',
            'technologies': [
                technologies['Python'],
                technologies['Django'],
                technologies['HTML'],
                technologies['CSS'],
                technologies['PostgreSQL'],
            ],
            'order': 1,
        },
        {
            'name': 'Desafio Codificador de Texto',
            'name_en': 'Text Encoder Challenge',
            'image': File(open(projects['Desafio Codificador de Texto'], 'rb')),
            'repository': 'https://github.com/JVMartyns/alura_one_encryptor_challenge',
            'description': 'Desafio da Formação Iniciante em Programação T5 - ONE do programa de formação Alura - Oracle Next formation.',
            'description_en': 'Challenge from the "Formação Iniciante em Programação T5 - ONE" course of the Alura - Oracle Next Education program.',
            'technologies': [
                technologies['HTML'],
                technologies['CSS'],
                technologies['JavaScript'],
            ],
            'order': 2,
        },
        {
            'name': 'Desafio Bank API Cumbuca',
            'name_en': 'Challenge Cumbuca Bank API',
            'image': File(open(projects['Desafio Bank API Cumbuca'], 'rb')),
            'repository': 'https://github.com/JVMartyns/cumbuca-challenge',
            'description': 'API de conta bancária desenvolvida em Elixir e Phoenix com banco de dados PostgreSQL. Permite o cadastro de contas bancárias e execução de transações financeiras.',
            'description_en': 'Bank account API developed in Elixir and Phoenix with PostgreSQL database. Allows registration of bank accounts and execution of financial transactions.',
            'technologies': [
                technologies['Elixir'],
                technologies['Phoenix'],
                technologies['PostgreSQL'],
            ],
            'order': 3,
        }
    ]

    for seed_data in seeds:
        try:
            project = Project.objects.create(
                name=seed_data['name'],
                name_en=seed_data['name_en'],
                image=seed_data['image'],
                repository=seed_data['repository'],
                description=seed_data['description'],
                description_en=seed_data['description_en'],
                order=seed_data['order'],
            )
            project.technologies.set(seed_data['technologies'])
        except IntegrityError:
            pass
