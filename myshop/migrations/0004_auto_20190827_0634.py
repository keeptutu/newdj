# Generated by Django 2.2.4 on 2019-08-26 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0003_auto_20190826_2104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'ordering': ['goods_id']},
        ),
    ]
