from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    SERVICE_TYPES = [
        ('WEBSITE', 'Criação de Sites'),
        ('CHATBOT', 'Chatbots com IA'),
        ('APP', 'Aplicações sob Demanda'),
    ]
    
    STATUS_CHOICES = [
        ('ACTIVE', 'Ativo'),
        ('INACTIVE', 'Inativo'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    short_description = models.TextField()
    description = models.TextField()
    features = models.TextField(help_text="Digite cada recurso em uma nova linha")
    price_from = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    is_featured = models.BooleanField(default=False)
    whatsapp_message = models.TextField(
        help_text="Mensagem predefinida para o WhatsApp",
        default="Olá! Gostaria de saber mais sobre o serviço de {service_name}."
    )
    whatsapp_number = models.CharField(
        max_length=20,
        help_text="Número do WhatsApp com código do país (ex: 5511999999999)"
    )
    featured_image = models.ImageField(
        upload_to='services/featured/',
        blank=True,
        null=True,
        help_text="Imagem principal do serviço"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def feature_list(self):
        """Returns features as a list"""
        return [f.strip() for f in self.features.split('\n') if f.strip()]

    def get_whatsapp_link(self):
        """Generate WhatsApp link with predefined message"""
        message = self.whatsapp_message.format(service_name=self.name)
        return f"https://wa.me/{self.whatsapp_number}?text={message}"

class ServiceProject(models.Model):
    service = models.ForeignKey(Service, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(
        upload_to='services/projects/',
        help_text="Imagem do projeto"
    )
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service.name} - {self.title}"

class ServiceFAQ(models.Model):
    service = models.ForeignKey(Service, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.service.name} - {self.question}"
