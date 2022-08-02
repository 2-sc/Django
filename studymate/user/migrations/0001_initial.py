# Generated by Django 3.2 on 2022-08-02 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=32, verbose_name='아이디')),
                ('username', models.CharField(max_length=32, verbose_name='이름')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_contents', models.TextField(verbose_name='간단한 소개')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'verbose_name': '유저프로필',
                'verbose_name_plural': '유저프로필',
                'db_table': 'user_profile',
            },
        ),
    ]
