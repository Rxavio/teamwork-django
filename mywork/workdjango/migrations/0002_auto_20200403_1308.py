# Generated by Django 3.0.3 on 2020-04-03 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workdjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
