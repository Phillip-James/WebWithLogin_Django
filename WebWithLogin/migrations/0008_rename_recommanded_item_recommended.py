# Generated by Django 5.1.2 on 2024-11-06 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebWithLogin', '0007_rename_recommended_item_recommanded'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='recommanded',
            new_name='recommended',
        ),
    ]
