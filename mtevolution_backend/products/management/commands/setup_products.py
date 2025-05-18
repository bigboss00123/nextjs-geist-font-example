from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Setup initial products'

    def handle(self, *args, **kwargs):
        # Zamba E-commerce
        zamba = Product.objects.create(
            name='Zamba',
            product_type='ZAMBA',
            short_description='Sistema de vendas online com entregas grátis',
            description='''
            Zamba é uma plataforma de e-commerce completa que permite que você venda seus produtos online com entregas grátis.
            Com uma interface moderna e intuitiva, o Zamba oferece uma experiência de compra excepcional para seus clientes.
            ''',
            features='''
            - Gestão completa de produtos e estoque
            - Sistema de entregas grátis integrado
            - Pagamentos online seguros
            - Painel administrativo intuitivo
            - Relatórios detalhados de vendas
            - Integração com marketplaces
            ''',
            status='LIVE',
            is_featured=True,
            url='https://zamba.mtevolution.com'
        )

        # Kubuca Cursos
        kubuca = Product.objects.create(
            name='Kubuca',
            product_type='KUBUCA',
            short_description='Plataforma de cursos online',
            description='''
            Kubuca é uma plataforma de educação online que conecta instrutores e alunos.
            Oferece uma experiência de aprendizado interativa e envolvente com recursos modernos.
            ''',
            features='''
            - Sistema de videoaulas HD
            - Material didático digital
            - Certificados automáticos
            - Fórum de discussão
            - Avaliações e exercícios
            - App mobile para estudos offline
            ''',
            status='LIVE',  # Changed from DEVELOPMENT to LIVE
            is_featured=True
        )

        # Afri'IA WhatsApp
        afriia = Product.objects.create(
            name="Afri'IA",
            product_type='AFRIIA',
            short_description='Inteligência Artificial no WhatsApp',
            description='''
            Afri'IA é um assistente virtual inteligente que opera através do WhatsApp,
            oferecendo suporte 24/7 para seus clientes com respostas personalizadas e contextualmente relevantes.
            ''',
            features='''
            - Respostas automáticas inteligentes
            - Processamento de linguagem natural
            - Integração com sistemas externos
            - Análise de sentimento
            - Relatórios de interação
            - Personalização de respostas
            ''',
            status='LIVE',  # Changed from DEVELOPMENT to LIVE
            is_featured=True
        )

        # API WhatsApp
        whatsapp = Product.objects.create(
            name='API WhatsApp',
            product_type='WHATSAPP',
            short_description='Plataforma de integração WhatsApp',
            description='''
            Nossa API WhatsApp permite integrar o WhatsApp Business com seus sistemas existentes,
            automatizando comunicações e melhorando o atendimento ao cliente.
            ''',
            features='''
            - Envio automatizado de mensagens
            - Webhooks para eventos
            - Dashboard de métricas
            - Gestão de múltiplos números
            - Templates de mensagem
            - Suporte técnico especializado
            ''',
            status='LIVE',  # Changed from DEVELOPMENT to LIVE
            is_featured=True
        )

        self.stdout.write(self.style.SUCCESS('Successfully created initial products'))
