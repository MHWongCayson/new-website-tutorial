# Generated by Django 5.0.1 on 2024-01-22 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
    ]
