from core.models import Formation, Institution


def execute_seeds():
    seeds = [
        Formation(
            name='Ensino Médio',
            degree='High School',
            institution=Institution.objects.get(
                name='Escola Municipal Manoel Teodoro de Arruda'
            ),
            start_date='2013-02-01',
            end_date='2015-12-22',
            status='Completed'
        ),
        Formation(
            name='Informática para Internet',
            degree='Technical',
            institution=Institution.objects.get(
                name='Instituto Federal de Educação, Ciência e Tecnologia - IFPE'
            ),
            start_date='2016-02-01',
            end_date='2017-12-22',
            status='Incomplete'
        ),
    ]

    Formation.objects.bulk_create(seeds, ignore_conflicts=True)
