# Generated by Django 3.1.2 on 2020-10-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_usertravel_places'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertravel',
            name='places',
            field=models.TextField(default='[]', max_length=1000, null=True),
        ),
    ]
