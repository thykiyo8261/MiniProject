# Generated by Django 4.0.2 on 2022-02-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
