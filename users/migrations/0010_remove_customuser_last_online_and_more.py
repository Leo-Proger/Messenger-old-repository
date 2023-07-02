# Generated by Django 4.2 on 2023-06-12 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_customuser_status_alter_customuser_last_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='last_online',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='status',
        ),
        migrations.CreateModel(
            name='ConnectionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=100, verbose_name='id устройства')),
                ('connection_time', models.DateTimeField(auto_now_add=True, verbose_name='Время подключения')),
                ('disconnection_time', models.DateTimeField(blank=True, null=True, verbose_name='Время отключения')),
                ('last_online', models.DateTimeField(blank=True, null=True, verbose_name='Время последнего входа')),
                ('online_count', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'device_id')},
            },
        ),
    ]
