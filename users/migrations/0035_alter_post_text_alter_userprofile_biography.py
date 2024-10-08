# Generated by Django 4.2.3 on 2023-08-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_remove_userprofile_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Текст поста'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='biography',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Биография'),
        ),
    ]
