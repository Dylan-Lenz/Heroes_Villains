# Generated by Django 4.1 on 2022-08-31 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0004_alter_supers_super_type'),
        ('super_type', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Super_types',
            new_name='Super_type',
        ),
    ]