# Generated by Django 3.0.5 on 2020-07-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0011_userdetail_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
