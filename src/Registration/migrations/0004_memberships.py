# Generated by Django 4.0.2 on 2022-02-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_alter_student_branch_alter_student_cont_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memberships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('regno', models.IntegerField(null=True)),
                ('branch', models.CharField(max_length=100, null=True)),
                ('sem', models.IntegerField(null=True)),
                ('cont', models.IntegerField(null=True)),
                ('m_type', models.CharField(choices=[('Gym', 'Gym'), ('Swimming', 'Swimming'), ('Both', 'Both')], max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]