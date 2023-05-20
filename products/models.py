from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        verbose_name='Categoria',
        max_length=200,
        db_index=True
    )
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=200,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self) -> str:
        return self.name

    # def get_absolute_url(self):
    #     return reverse('shop:product_list_by_category',
    #                    args=[self.slug])

    
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name='Categoria do produto',
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Nome do produto',
        max_length=200,
        db_index=True
    )
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=200,
        unique=True
    )
    image = models.ImageField(
        verbose_name='Imagem do produto',
        upload_to='products/',
        blank=True,
        null=True      
    )
    description = models.TextField(
        verbose_name='Descrição do produto',
        blank=True,
        null=True
    )
    price = models.DecimalField(
        verbose_name='Preço do produto',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    available = models.BooleanField(
        verbose_name='Disponível',
        default=True
    )
    created = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Data de atualização',
        auto_now=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('shop:product_detail',
    #                    args=[self.id, self.slug])