# Generated by Django 3.2.5 on 2022-05-12 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_msg_msg_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='msg_type',
            field=models.BooleanField(default=False),
        ),
    ]