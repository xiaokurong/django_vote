# Generated by Django 2.0 on 2019-10-21 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investigateuserinfo',
            name='user_investigator',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='invert_date',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='investigated_user',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='investigator',
        ),
        migrations.AddField(
            model_name='answer',
            name='investigator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vote.Investigator', verbose_name='调查员'),
        ),
        migrations.AlterField(
            model_name='investigateuserinfo',
            name='user_countryside',
            field=models.CharField(max_length=20, null=True, verbose_name='乡'),
        ),
        migrations.AlterField(
            model_name='investigateuserinfo',
            name='user_village',
            field=models.CharField(max_length=30, null=True, verbose_name='村'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_E',
            field=models.CharField(max_length=30, null=True, verbose_name='E'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_F',
            field=models.CharField(max_length=30, null=True, verbose_name='F'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_G',
            field=models.CharField(max_length=30, null=True, verbose_name='G'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_H',
            field=models.CharField(max_length=30, null=True, verbose_name='H'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_I',
            field=models.CharField(max_length=30, null=True, verbose_name='I'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_J',
            field=models.CharField(max_length=30, null=True, verbose_name='J'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_K',
            field=models.CharField(max_length=30, null=True, verbose_name='K'),
        ),
    ]