# Generated by Django 4.2.7 on 2023-12-11 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManagementSystem', '0002_alter_invoice_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='id',
            new_name='idC',
        ),
    ]
