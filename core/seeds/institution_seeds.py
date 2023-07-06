from django.core.files import File
from core.models import Institution


def execute_seeds():
    institution = {
        'EMMTA': 'media_aux/institutions/emmta.svg',
        'IFPE': 'media_aux/institutions/ifpe.svg',
        'Curso em Video': 'media_aux/institutions/curso_em_video.svg',
        'Udemy': 'media_aux/institutions/udemy.svg',
        'Alura': 'media_aux/institutions/alura.svg',
        'Exercito': 'media_aux/institutions/exercito_brasileiro.svg',
        'PlugCamp': 'media_aux/institutions/plug_camp.svg',
    }

    seeds = [
        Institution(
            name='Escola Municipal Manoel Teodoro de Arruda',
            image=File(open(institution['EMMTA'], 'rb')),
            site='https://www.instagram.com/manoelteodoro.sv'
        ),
        Institution(
            name='Instituto Federal de Educação, Ciência e Tecnologia - IFPE',
            image=File(open(institution['IFPE'], 'rb')),
            site='https://www.ifpe.edu.br/campus/belo-jardim'
        ),
        Institution(
            name='Curso em Video',
            image=File(open(institution['Curso em Video'], 'rb')),
            site='https://www.cursoemvideo.com'
        ),
        Institution(
            name='Udemy',
            image=File(open(institution['Udemy'], 'rb')),
            site='https://www.udemy.com/'
        ),
        Institution(
            name='Alura',
            image=File(open(institution['Alura'], 'rb')),
            site='https://www.alura.com.br/'
        ),
        Institution(
            name='Exercito Brasileiro',
            image=File(open(institution['Exercito'], 'rb')),
            site='https://10ciaecmb.eb.mil.br/'
        ),
        Institution(
            name='PlugCamp',
            image=File(open(institution['PlugCamp'], 'rb')),
            site='https://plug.camp/'
        )
    ]

    Institution.objects.bulk_create(seeds, ignore_conflicts=True)
