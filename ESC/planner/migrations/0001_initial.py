# Generated by Django 4.1.1 on 2022-10-01 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=50, verbose_name='todo')),
                ('complete', models.BooleanField()),
                ('schedule', models.CharField(max_length=50, verbose_name='schedule')),
                ('post_text', models.CharField(max_length=20, verbose_name='post text')),
                ('register', models.DateTimeField(verbose_name='today')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
