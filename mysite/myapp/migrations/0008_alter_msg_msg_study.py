# Generated by Django 3.2.5 on 2022-05-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20220512_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='msg_study',
            field=models.CharField(blank=True, choices=[('nako', 'NAKO'), ('resist', 'RESIST')], max_length=200, null=True),
        ),
    ]
