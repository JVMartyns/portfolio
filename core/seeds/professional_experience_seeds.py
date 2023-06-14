from core.models import ProfessionalExperience


def execute_seeds():
    seeds = [
        ProfessionalExperience(
            name='Desenvolvedor Backend',
            name_en='Backend Developer',
            company='Solfácil',
            start_date='2022-05-23',
            end_date='2023-02-03',
            description="- Participação em uma jornada do zero no desenvolvimento de um Sistema que atingiu 60% de ativação, superando o Key Result trimestral em 20% (50%).\n- Planejamento e desenvolvimento de software escalável e de alto desempenho usando Elixir e Phoenix com Banco de dados PostgreSQL e Redis, em conjunto com pipelines CI/CD.\n- Implementação de API's REST e GraphQL, Crawler de coleta, Parsers e criptografia para processamento e preservação de dados sensíveis, assegurando a integridade e confidencialidade das informações.\n- Utilização de ferramentas modernas de DevOps, como Git e GitHub, Docker, Jira, Trello, Jenkins, Rancher, Kafka, Grafana e Datadog, para otimizar o fluxo de desenvolvimento, garantir a qualidade do código e a integração contínua e a entrega contínua (CI/CD) do software.\n- Contribuição ativa para o desenvolvimento de soluções inovadoras e eficazes, visando aprimorar a experiência do usuário e a competitividade da fintech no mercado de energia solar.\n- Colaboração com uma equipe multifuncional, participando de reuniões de planejamento, revisões de código e compartilhando conhecimentos técnicos com colegas, contribuindo para um ambiente de trabalho colaborativo e produtivo.",
            description_en="- Participation in a journey from scratch in the development of a System that reached 60% activation, surpassing the quarterly Key Result by 20% (50%).\n- Planning and development of scalable, high-performance software using Elixir and Phoenix with PostgreSQL Database and Redis, in conjunction with CI/CD pipelines.\n- Implementation of API's REST and GraphQL, Crawler collection, Parsers and cryptography for processing and preservation of sensitive data, ensuring the integrity and confidentiality of information.\n- Use of modern DevOps tools such as Git and GitHub, Docker, Jira, Trello, Jenkins, Rancher, Kafka, Grafana and Datadog to optimize the development flow, ensure code quality and continuous integration and continuous delivery (CI /CD) of the software.\n- Active contribution to the development of innovative and effective solutions, aiming to improve the user experience and fintech's competitiveness in the solar energy market.\n- Collaboration with a cross-functional team, participating in planning meetings, code reviews and sharing technical knowledge with colleagues, contributing to a collaborative and productive work environment."
        ),
        ProfessionalExperience(
            name='Porteiro - Segurança Patrimonial',
            name_en='Doorman - Asset Security',
            company='Liserve',
            start_date='2019-08-15',
            end_date='2022-05-19',
            description='- Realização do controle de acesso de pessoas, veículos, materiais e ferramentas às instalações do complexo, garantindo a segurança e integridade do patrimônio.\n- Execução de revista pessoal, veicular e inspeção de materiais, assegurando o cumprimento das normas e procedimentos de segurança estabelecidos.\n- Responsável pela pesagem de veículos e materiais, verificação de Notas Fiscais e cargas, garantindo a conformidade e registro adequado de informações.\n- Análise e tratamento de solicitações, fornecendo informações corretas sobre setores, normas e procedimentos aos colaboradores e visitantes, garantindo o correto encaminhamento de demandas.\n- Atendimento cortês e profissional às pessoas que buscam acesso às instalações, mantendo a postura adequada e demonstrando habilidades interpessoais eficazes.',
            description_en='- Control of access for individuals, vehicles, materials, and tools to the complex facilities, ensuring security and asset integrity.\n- Conducting personal, vehicle, and material searches and inspections to ensure compliance with established security norms and procedures.\n- Responsible for weighing vehicles and materials, verifying invoices and shipments, ensuring conformity and proper recording of information.\n- Analysis and handling of inquiries, providing accurate information about departments, norms, and procedures to employees and visitors, ensuring proper routing of requests.\n- Courteous and professional assistance to individuals seeking access to the facilities, maintaining appropriate posture and demonstrating effective interpersonal skills.'
        ),
        ProfessionalExperience(
            name='Auxiliar de informática',
            name_en='IT Assistant',
            company='Exército Brasileiro',
            start_date='2018-02-01',
            end_date='2019-03-31',
            description='- Prestação de suporte técnico especializado, diagnóstico e solução de falhas de hardware e software, garantindo a rápida recuperação de sistemas e minimizando o tempo de inatividade.\n- Colaboração ativa com outros departamentos, fornecendo suporte técnico em eventos e treinamentos, assegurando a continuidade das atividades operacionais e contribuindo para o sucesso das missões realizadas.\n- Realização de manutenção e formatação de Desktops, Notebooks e outros dispositivos, para garantir o desempenho e a confiabilidade dos equipamentos.\n- Instalação e manutenção de redes, sistemas operacionais, softwares e periféricos, visando a otimização e a disponibilidade dos recursos de TI, bem como a melhoria contínua da infraestrutura tecnológica.',
            description_en='- Provision of specialized technical support, diagnosis, and resolution of hardware and software failures, ensuring quick system recovery and minimizing downtime.\n- Active collaboration with other departments, providing technical support during events and training sessions, ensuring the continuity of operational activities and contributing to the success of missions.\n- Maintenance and formatting of desktops, laptops, and other devices to ensure performance and reliability of equipment.\n- Installation and maintenance of networks, operating systems, software, and peripherals, aiming to optimize IT resources and improve the technological infrastructure continuously.'
        )
    ]

    ProfessionalExperience.objects.bulk_create(seeds, ignore_conflicts=True)
