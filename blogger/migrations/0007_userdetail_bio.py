# Generated by Django 3.0.5 on 2020-07-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0006_auto_20200724_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='bio',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]