# Generated by Django 3.1 on 2020-08-29 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='title',
            field=models.CharField(default='default title', max_length=100),
        ),
    ]
