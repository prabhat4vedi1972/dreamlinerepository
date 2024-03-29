# Generated by Django 2.2.3 on 2019-07-19 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0003_auto_20190719_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(error_messages={'required': 'Please provide your email address.', 'unique': 'An account with this email exist.'}, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.IntegerField(max_length=14),
        ),
    ]
