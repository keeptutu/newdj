# Generated by Django 2.2.4 on 2019-08-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_goods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
