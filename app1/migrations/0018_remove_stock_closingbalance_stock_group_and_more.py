# Generated by Django 4.0.5 on 2022-09-28 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_stock_closingbalance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_closingbalance',
            name='stock_group',
        ),
        migrations.RemoveField(
            model_name='stock_closingbalance',
            name='stock_item',
        ),
    ]
