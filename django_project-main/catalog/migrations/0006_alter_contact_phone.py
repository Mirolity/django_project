# Generated by Django 4.0.4 on 2025-02-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон'),
        ),
    ]
