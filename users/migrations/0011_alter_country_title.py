# Generated by Django 4.1.7 on 2023-04-26 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Country'),
        ),
    ]
