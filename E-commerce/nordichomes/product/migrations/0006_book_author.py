# Generated by Django 5.0.1 on 2024-01-22 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_name_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
