# Generated by Django 4.1.3 on 2022-11-29 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("traits", "0002_trait_create_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trait",
            name="pets",
        ),
    ]