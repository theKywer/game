# Generated by Django 5.0.6 on 2024-06-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamewarrior', '0007_alter_game_imagecar1_alter_game_imagecar2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.TextField(default=''),
        ),
    ]
