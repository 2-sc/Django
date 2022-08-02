# Generated by Django 3.2 on 2022-08-02 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField(verbose_name='내용')),
                ('dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('writer', models.ForeignKey(db_column='writer', on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'verbose_name': '담벼락',
                'verbose_name_plural': '담벼락',
                'db_table': 'board',
            },
        ),
    ]
