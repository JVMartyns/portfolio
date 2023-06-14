from django.core.files import File
from core.models import Profile


def execute_seeds():
    profile_image_path = 'media_aux/profile/profile.jpg'
    seeds = [
        Profile(
            first_name='João Vitor',
            last_name='Martins Araújo',
            image=File(open(profile_image_path, 'rb')),
            description="Olá, meu nome é João Vitor e sou desenvolvedor de sistemas. Gosto de ver animes, séries e filmes. Também gosto de ler livros de conteúdo técnico de ficção. Sou apaixonado por tecnologias e estou sempre buscando aprender coisas novas.\nAtualmente o meu foco é no Backend com Elixir e Python.Já trabalhei com times de desenvolvimento ágeis usando o modelo Spotify. Sou familiarizado com metodologias como Scrum e Kanban. Já participei de todas as etapas de desenvolvimento de um produto, desde a idealização com gestores de produto e designers ux/ui, até a construção com meus pares desenvolvedores e techlead.",
            description_en="Hello, my name is João Vitor, and I am a systems developer. I enjoy watching anime, series, and movies. I also like reading books with technical and fictional content. I am passionate about technology and always strive to learn new things.\nCurrently, my focus is on Backend development with Elixir and Python. I have previously worked with agile development teams following the Spotify model. I am familiar with methodologies such as Scrum and Kanban. I have been involved in all stages of product development, from ideation with product managers and UX/UI designers to implementation with fellow developers and tech leads.",
        )
    ]

    Profile.objects.bulk_create(seeds, ignore_conflicts=True)
