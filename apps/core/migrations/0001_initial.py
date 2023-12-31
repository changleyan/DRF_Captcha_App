# Generated by Django 4.2.2 on 2023-09-16 20:36

import apps.core.api.v1.captcha_component.CaptchaModel
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupp',
            fields=[
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'permissions': (('list_group', 'Can list groups'),),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='Captcha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('expiration_date', models.DateTimeField(default=apps.core.api.v1.captcha_component.CaptchaModel.calcular_expiration_time)),
                ('uuid', models.CharField(max_length=250, unique=True)),
                ('pass_captcha', models.BooleanField(default=False)),
                ('captcha_text', models.TextField(max_length=10)),
            ],
            options={
                'verbose_name': 'Captcha',
                'verbose_name_plural': 'Captchas',
                'ordering': ['-date', '-id'],
                'indexes': [models.Index(fields=['uuid'], name='uuid_idx')],
            },
        ),
    ]
