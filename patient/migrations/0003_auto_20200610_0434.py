# Generated by Django 3.0.5 on 2020-06-10 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]