# Generated by Django 4.2.7 on 2023-12-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagementSystem', '0003_rename_id_invoice_idc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='idC',
        ),
        migrations.AddField(
            model_name='invoice',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]