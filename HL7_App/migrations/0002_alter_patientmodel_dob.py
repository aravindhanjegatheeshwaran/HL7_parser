# Generated by Django 5.0.7 on 2024-07-21 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HL7_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmodel',
            name='dob',
            field=models.DateField(blank=True),
        ),
    ]
