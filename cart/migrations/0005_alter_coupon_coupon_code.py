# Generated by Django 4.1.1 on 2022-10-02 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_coupon_usedcoupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_code',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
