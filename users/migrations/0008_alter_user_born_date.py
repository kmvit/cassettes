# Generated by Django 4.1.7 on 2023-03-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_born_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='born_date',
            field=models.DateField(blank=True),
        ),
    ]