# Generated by Django 3.2.5 on 2022-05-18 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20220512_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='msg_room',
            field=models.CharField(blank=True, choices=[('Labor', 'Labor'), ('U1', 'U1'), ('U2', 'U2'), ('U3', 'U3'), ('U4', 'U4')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='msg',
            name='msg_study',
            field=models.CharField(blank=True, choices=[('NAKO', 'NAKO'), ('RESIST', 'RESIST')], max_length=200, null=True),
        ),
    ]
