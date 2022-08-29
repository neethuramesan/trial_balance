# Generated by Django 4.0.2 on 2022-08-29 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_payitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='payable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('party_name', models.CharField(max_length=255)),
                ('pending_amound', models.IntegerField()),
                ('due_date', models.DateField()),
                ('overdue', models.IntegerField(null=True)),
                ('items', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.payitems')),
            ],
        ),
    ]
