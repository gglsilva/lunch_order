from django.db import models
from django.urls import reverse
from account.models import Profile
from products.models import Product
    

class Order(models.Model):
    client = models.ForeignKey(
        Profile,
        verbose_name='Cliente',
        related_name='cliente_orders',
        on_delete=models.CASCADE,
    )
    note = models.TextField(
        verbose_name='Observação',
        blank=True,
        null=True
    )
    created = models.DateField(
        verbose_name='Data de criação',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Data de atualização',
        auto_now=True
    )
    class Meta:
        ordering = ('-created',)
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self) -> str:
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    @property
    def get_product_for_order(self):
        return ''.join(f'{item.product.name}, ' for item in self.items.all())
    
    @property
    def return_note_with_string(self):
        return f'{self.note}' if self.note else ''


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name='Pedido',
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Produto',
        related_name='order_items',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        verbose_name='Preço',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Quantidade',
        default=1
    )
    created = models.DateField(
        verbose_name='Data de criação',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Data de atualização',
        auto_now=True
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Item Pedido'
        verbose_name_plural = 'Itens Pedidos'

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

    @property
    def get_produt_quantity(self):
        return f'{self.product.name} + {self.quantity}'
    