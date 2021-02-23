# Generated by Django 3.1.5 on 2021-02-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_auto_20210223_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='avg_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='geek_rating',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]