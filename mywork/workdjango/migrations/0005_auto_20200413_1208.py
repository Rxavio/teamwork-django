# Generated by Django 3.0.3 on 2020-04-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workdjango', '0004_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=45),
        ),
    ]
