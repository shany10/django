# Generated by Django 4.2.6 on 2023-11-06 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Secretary', 'Secretary'), ('Insctructor', 'Insctructor'), ('Student', 'Student')], default='', max_length=30),
        ),
    ]
