# Generated by Django 4.2.7 on 2023-12-11 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagementSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
