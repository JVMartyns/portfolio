from core.models import Course, Institution


def execute_seeds():
    institutions = {
        'Udemy': Institution.objects.get(name='Udemy'),
        'Curso em Video': Institution.objects.get(name='Curso em Video'),
        'Alura': Institution.objects.get(name='Alura'),
        'Exercito': Institution.objects.get(name='Exercito Brasileiro'),
        'PlugCamp': Institution.objects.get(name='PlugCamp'),
        'EMMTA': Institution.objects.get(name='Escola Municipal Manoel Teodoro de Arruda'),
        'IFPE': Institution.objects.get(name='Instituto Federal de Educação, Ciência e Tecnologia - IFPE'),
    }

    seeds = [
        Course(
            name='Python 3',
            institution=institutions['Curso em Video'],
            workload=120,
            certification_date='2022-01-01',
            certificate_link='https://drive.google.com/file/d/1k_2umvcVh4P8rmsbY5EwfP9Ilea60UiJ/view?usp=sharing',
        ),
        Course(
            name='BootCamp Elixir',
            institution=institutions['PlugCamp'],
            workload=90,
            certification_date='2022-04-14',
            certificate_link='https://drive.google.com/file/d/1hvjEHjsc9ufL8BpNrC-3XbpIXLrZSQ0P/view?usp=sharing',
        ),
        Course(
            name='Elixir e Phoenix do Zero!',
            institution=institutions['Udemy'],
            workload=11,
            certification_date='2022-05-27',
            certificate_link='https://www.udemy.com/certificate/UC-e0de6094-3404-462c-afbe-67d347943cf1/',
        ),
    ]

    Course.objects.bulk_create(seeds,  ignore_conflicts=True)
