# Generated by Django 5.0.1 on 2024-08-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("system", "0008_alter_transactions_reciver_alter_transactions_sender"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="phone_number",
            field=models.IntegerField(blank=True, default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="amount",
            field=models.FloatField(blank=True),
        ),
    ]
