# Generated by Django 3.1.5 on 2021-02-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
    ]
