# Generated by Django 4.0.2 on 2022-02-11 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0004_memberships'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Memberships',
            new_name='Membership',
        ),
    ]
