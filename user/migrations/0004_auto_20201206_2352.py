# Generated by Django 3.1.3 on 2020-12-06 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_phoneauth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneauth',
            name='auth_number',
            field=models.IntegerField(),
        ),
    ]
