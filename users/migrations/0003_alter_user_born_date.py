# Generated by Django 4.1.7 on 2023-03-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='born_date',
            field=models.DateField(blank=True),
        ),
    ]