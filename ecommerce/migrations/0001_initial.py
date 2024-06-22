# Generated by Django 5.0.6 on 2024-06-22 11:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gamewarrior', '0010_remove_orderlist_order_id_remove_orderlist_game_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('status', models.BooleanField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('id_game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game', to='gamewarrior.game')),
                ('id_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='ecommerce.order')),
            ],
        ),
    ]
