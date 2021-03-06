# Generated by Django 2.0 on 2019-10-21 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_A', models.BooleanField(choices=[(0, 'N'), (1, 'Y')], default=0)),
                ('question_B', models.BooleanField(choices=[(0, 'N'), (1, 'Y')], default=0)),
                ('question_C', models.BooleanField(choices=[(0, 'N'), (1, 'Y')], default=0)),
                ('question_D', models.BooleanField(choices=[(0, 'N'), (1, 'Y')], default=0)),
                ('question_E', models.BooleanField(choices=[(0, 'N'), (1, 'Y')], default=0)),
                ('question_F', models.BooleanField(choices=[(0, 'N'), (1, 'Y')], default=0)),
                ('question_G', models.BooleanField(choices=[(0, 'N'), (1, 'Y')], default=0)),
                ('question_H', models.BooleanField(choices=[(0, 'N'), (1, 'Y')], default=0)),
                ('question_I', models.BooleanField(choices=[(0, 'N'), (1, 'Y')], default=0)),
                ('question_J', models.BooleanField(choices=[(0, 'N'), (1, 'Y')], default=0)),
                ('question_K', models.CharField(max_length=125, verbose_name='其他')),
            ],
        ),
        migrations.CreateModel(
            name='InvestigateUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25, verbose_name='姓名')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加日期')),
                ('user_age', models.IntegerField(null=True, verbose_name='年龄')),
                ('user_sex', models.BooleanField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别')),
                ('user_countryside', models.CharField(max_length=20, verbose_name='乡')),
                ('user_village', models.CharField(max_length=30, verbose_name='村')),
                ('user_poor_type', models.BooleanField(choices=[(0, '是'), (1, '否')], default=1, verbose_name='贫困户')),
                ('user_ill_type', models.CharField(max_length=50, null=True, verbose_name='疾病类型')),
                ('user_speical_human', models.CharField(max_length=50, null=True, verbose_name='特殊人群')),
            ],
        ),
        migrations.CreateModel(
            name='Investigator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25, verbose_name='姓名')),
                ('user_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=128, verbose_name='问题')),
                ('type_select', models.IntegerField(choices=[(1, '单选'), (2, '多选'), (3, '问答')])),
                ('question_A', models.CharField(max_length=30, verbose_name='A')),
                ('question_B', models.CharField(max_length=30, verbose_name='B')),
                ('question_C', models.CharField(max_length=30, verbose_name='C')),
                ('question_D', models.CharField(max_length=30, verbose_name='D')),
                ('question_E', models.CharField(max_length=30, verbose_name='E')),
                ('question_F', models.CharField(max_length=30, verbose_name='F')),
                ('question_G', models.CharField(max_length=30, verbose_name='G')),
                ('question_H', models.CharField(max_length=30, verbose_name='H')),
                ('question_I', models.CharField(max_length=30, verbose_name='I')),
                ('question_J', models.CharField(max_length=30, verbose_name='J')),
                ('question_K', models.CharField(max_length=30, verbose_name='K')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionNaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='问卷标题')),
                ('invert_date', models.DateTimeField(auto_now_add=True, verbose_name='调查时间')),
                ('investigated_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vote.InvestigateUserInfo', verbose_name='调查用户')),
                ('investigator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vote.Investigator', verbose_name='调查员')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='qestionnaire',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='vote.QuestionNaire', verbose_name='该问卷下的问题'),
        ),
        migrations.AddField(
            model_name='investigateuserinfo',
            name='user_investigator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vote.Investigator', verbose_name='调查员'),
        ),
        migrations.AddField(
            model_name='answer',
            name='invest_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vote.InvestigateUserInfo', verbose_name='调查用户'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Question', verbose_name='问题'),
        ),
    ]
