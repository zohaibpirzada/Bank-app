# Generated by Django 5.1 on 2024-08-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0017_alter_transactions_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
