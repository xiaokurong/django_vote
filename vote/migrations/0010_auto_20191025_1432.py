# Generated by Django 2.0 on 2019-10-25 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0009_auto_20191024_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='qestionnaire',
            new_name='questionnaire',
        ),
    ]
