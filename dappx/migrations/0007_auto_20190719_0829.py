# Generated by Django 2.2.3 on 2019-07-19 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0006_auto_20190719_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.IntegerField(max_length=10, unique=True),
        ),
    ]
