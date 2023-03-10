# Generated by Django 4.1.5 on 2023-02-17 21:47

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ("contact_generator", "0003_alter_contact_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="number",
            field=phone_field.models.PhoneField(blank=True, help_text="Contact phone number", max_length=31),
        ),
    ]
