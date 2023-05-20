# Generated by Django 4.2.1 on 2023-05-20 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_orders', to='account.profile', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Preço')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order', verbose_name='Pedido')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.product', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Item Pedido',
                'verbose_name_plural': 'Itens Pedidos',
                'ordering': ('-created',),
            },
        ),
    ]
