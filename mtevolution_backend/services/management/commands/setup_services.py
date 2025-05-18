from django.core.management.base import BaseCommand
from services.models import Service, ServiceFAQ

class Command(BaseCommand):
    help = 'Create initial services'

    def handle(self, *args, **kwargs):
        services_data = [
            {
                'name': 'Criação de Sites',
                'service_type': 'WEBSITE',
                'short_description': 'Sites profissionais e responsivos para sua empresa',
                'description': '''
Desenvolvemos sites modernos e profissionais que se adaptam a qualquer dispositivo.
Nossos sites são:
- Responsivos (adaptam-se a celulares e tablets)
- Otimizados para SEO
- Rápidos e seguros
- Fáceis de atualizar
- Integrados com redes sociais
                ''',
                'features': '''
Design personalizado
Otimização para SEO
Responsivo para mobile
Integração com redes sociais
Painel administrativo
Hospedagem inclusa
Certificado SSL
Suporte técnico
                ''',
                'price_from': 2500.00,
                'whatsapp_number': '5511999999999',
                'whatsapp_message': 'Olá! Gostaria de saber mais sobre o serviço de criação de sites.',
                'is_featured': True,
            },
            {
                'name': 'Chatbots com IA',
                'service_type': 'CHATBOT',
                'short_description': 'Automatize seu atendimento com chatbots inteligentes',
                'description': '''
Desenvolva chatbots inteligentes que utilizam IA para:
- Automatizar atendimento ao cliente
- Qualificar leads
- Responder perguntas frequentes
- Realizar vendas
- Coletar feedback
                ''',
                'features': '''
Inteligência Artificial avançada
Integração com WhatsApp
Personalização completa
Relatórios detalhados
Aprendizado contínuo
Multicanal
Suporte 24/7
                ''',
                'price_from': 1500.00,
                'whatsapp_number': '5511999999999',
                'whatsapp_message': 'Olá! Gostaria de saber mais sobre o serviço de chatbots com IA.',
                'is_featured': True,
            },
            {
                'name': 'Aplicações sob Demanda',
                'service_type': 'APP',
                'short_description': 'Desenvolvimento de aplicações personalizadas',
                'description': '''
Desenvolvemos aplicações sob medida para sua empresa:
- Sistemas web
- Aplicativos mobile
- Integrações com APIs
- Automação de processos
- Dashboards e relatórios
                ''',
                'features': '''
Análise de requisitos
Design de interface
Desenvolvimento ágil
Testes automatizados
Documentação completa
Treinamento da equipe
Suporte contínuo
                ''',
                'price_from': 5000.00,
                'whatsapp_number': '5511999999999',
                'whatsapp_message': 'Olá! Gostaria de saber mais sobre o serviço de desenvolvimento de aplicações.',
                'is_featured': True,
            },
        ]

        faqs_data = {
            'Criação de Sites': [
                {
                    'question': 'Quanto tempo leva para criar um site?',
                    'answer': 'O prazo médio é de 2 a 4 semanas, dependendo da complexidade do projeto.',
                    'order': 1
                },
                {
                    'question': 'O site será responsivo?',
                    'answer': 'Sim, todos os nossos sites são responsivos e se adaptam a qualquer dispositivo.',
                    'order': 2
                }
            ],
            'Chatbots com IA': [
                {
                    'question': 'O chatbot funciona 24 horas?',
                    'answer': 'Sim, o chatbot funciona 24 horas por dia, 7 dias por semana.',
                    'order': 1
                },
                {
                    'question': 'É possível integrar com meu WhatsApp?',
                    'answer': 'Sim, oferecemos integração completa com WhatsApp Business API.',
                    'order': 2
                }
            ],
            'Aplicações sob Demanda': [
                {
                    'question': 'Vocês desenvolvem aplicativos mobile?',
                    'answer': 'Sim, desenvolvemos aplicativos para iOS e Android.',
                    'order': 1
                },
                {
                    'question': 'Como funciona o processo de desenvolvimento?',
                    'answer': 'Trabalhamos com metodologia ágil, com entregas incrementais e feedback constante.',
                    'order': 2
                }
            ]
        }

        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                name=service_data['name'],
                defaults=service_data
            )
            
            # Add FAQs
            if service.name in faqs_data:
                for faq_data in faqs_data[service.name]:
                    ServiceFAQ.objects.get_or_create(
                        service=service,
                        question=faq_data['question'],
                        defaults={
                            'answer': faq_data['answer'],
                            'order': faq_data['order']
                        }
                    )

        self.stdout.write(self.style.SUCCESS('Successfully created initial services'))
