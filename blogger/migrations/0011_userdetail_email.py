# Generated by Django 3.0.5 on 2020-07-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0010_auto_20200724_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(default='test@gmail.com', max_length=150),
        ),
    ]
