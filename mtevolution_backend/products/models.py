from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Product(models.Model):
    PRODUCT_TYPES = [
        ('ZAMBA', 'Zamba'),
        ('KUBUCA', 'Kubuca'),
        ('AFRIIA', 'Afri\'IA'),
        ('WHATSAPP', 'WhatsApp API'),
    ]
    
    STATUS_CHOICES = [
        ('LIVE', 'Live'),
        ('DEVELOPMENT', 'Development'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    short_description = models.TextField()
    description = models.TextField()
    features = models.TextField(help_text="Digite cada recurso em uma nova linha")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DEVELOPMENT')
    is_featured = models.BooleanField(default=False)
    url = models.URLField(blank=True, null=True)
    featured_image = models.ImageField(
        upload_to='products/featured/',
        blank=True,
        null=True,
        help_text="Imagem principal do produto"
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

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='products/gallery/',
        help_text="Imagem para a galeria do produto"
    )
    alt_text = models.CharField(
        max_length=200,
        blank=True,
        help_text="Texto alternativo para acessibilidade"
    )
    is_primary = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.product.name} - Image {self.order}"

    def save(self, *args, **kwargs):
        if self.is_primary:
            # Ensure only one primary image per product
            ProductImage.objects.filter(product=self.product, is_primary=True).update(is_primary=False)
        super().save(*args, **kwargs)

class Testimonial(models.Model):
    product = models.ForeignKey(Product, related_name='testimonials', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    rating = models.IntegerField(
        default=5,
        choices=[(i, str(i)) for i in range(1, 6)],
        help_text="Avaliação de 1 a 5 estrelas"
    )
    avatar = models.ImageField(
        upload_to='testimonials/',
        blank=True,
        null=True,
        help_text="Foto do autor do depoimento"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return f"{self.author} - {self.product.name}"
