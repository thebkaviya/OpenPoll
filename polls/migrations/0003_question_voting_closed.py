# Generated by Django 3.2.7 on 2021-09-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210915_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='voting_closed',
            field=models.BooleanField(default=False, verbose_name='voting closed'),
        ),
    ]
