# Generated by Django 2.0.5 on 2020-05-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='sell_time',
            field=models.DateTimeField(),
        ),
    ]
