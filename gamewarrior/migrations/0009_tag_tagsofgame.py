# Generated by Django 5.0.6 on 2024-06-22 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamewarrior', '0008_game_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='TagsOfGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gamewarrior.game')),
                ('id_tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gamewarrior.tag')),
            ],
        ),
    ]