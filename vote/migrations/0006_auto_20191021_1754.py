# Generated by Django 2.0 on 2019-10-21 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0005_auto_20191021_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question_K',
            field=models.CharField(blank=True, max_length=125, null=True, verbose_name='K. 其他'),
        ),
    ]