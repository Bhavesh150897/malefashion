# Generated by Django 4.1 on 2022-08-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fashion", "0014_brand_slug"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderplaced",
            old_name="stripe_payment_intent",
            new_name="razorpay_payment_id",
        ),
        migrations.AddField(
            model_name="orderplaced",
            name="order_id",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]