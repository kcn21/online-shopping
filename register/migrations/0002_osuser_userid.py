# Generated by Django 2.0.2 on 2018-04-06 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='osuser',
            name='userid',
            field=models.CharField(default=3, max_length=10),
            preserve_default=False,
        ),
    ]
