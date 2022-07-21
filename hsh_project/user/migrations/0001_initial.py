# Generated by Django 4.0.6 on 2022-07-20 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='유저이름')),
                ('password', models.CharField(max_length=64, verbose_name='패스워드')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'db_table': 'hsh_userinfo',
            },
        ),
    ]
