# Generated by Django 4.1.7 on 2023-03-30 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_born_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('English', 'Английский'), ('Russian', 'Русский'), ('Spanish', 'Испанский')], max_length=200),
        ),
    ]
