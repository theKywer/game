# Generated by Django 5.0.6 on 2024-06-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamewarrior', '0004_rename_image_game_imagecar1_game_imagecar2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id_user',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
