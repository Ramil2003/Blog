# Generated by Django 4.0.2 on 2022-03-01 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(default='', max_length=100, unique=True),
        ),
    ]
