# Generated by Django 4.1.1 on 2022-10-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_alter_planner_post_text_alter_planner_schedule_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planner',
            name='register',
            field=models.DateField(verbose_name='today'),
        ),
    ]
