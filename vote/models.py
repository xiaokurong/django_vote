from django.db import models

# Create your models here.
class Investigator(models.Model):
    user_name = models.CharField(verbose_name='姓名',max_length=25)
    user_password = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name



class InvestigateUserInfo(models.Model):
    user_name = models.CharField(verbose_name='姓名',max_length=25)
    add_date = models.DateTimeField(verbose_name='添加日期',auto_now_add=True)
    user_age = models.IntegerField(verbose_name='年龄',null=True)
    user_sex = models.BooleanField(verbose_name='性别',choices=((0,'男'),(1,'女')),default=0)
    user_countryside = models.CharField(verbose_name='乡',max_length=20,null=True)
    user_village = models.CharField(verbose_name='村',max_length=30,null=True)
    user_poor_type = models.BooleanField(verbose_name='贫困户',choices=((0,'是'),(1,'否')),default=1)
    user_ill_type = models.CharField(verbose_name='疾病类型',max_length=50,null=True,)
    speical_human_type=((0,'残疾人'),(1,'孕妇'),(2,'儿童'),(3,'65岁以上老人'),(10,'否'))
    user_speical_human = models.IntegerField(verbose_name='特殊人群',choices=speical_human_type,default=10)
    objects = models.Manager()

    def __str__(self):
        return self.user_name



class QuestionNaire(models.Model):
    title = models.CharField(max_length=64,verbose_name='问卷标题')


    def __str__(self):
        return self.title


class QuestionType(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Question(models.Model):
    caption=models.CharField(max_length=128,verbose_name='问题')
    # question_type = ((1,'单选'),(2,'多选'),(3,'问答'))
    # type_select = models.IntegerField(choices=question_type)
    question_type = models.ForeignKey(to=QuestionType,verbose_name='问题类型',default=1,on_delete=models.DO_NOTHING)
    questionnaire = models.ForeignKey(to=QuestionNaire,verbose_name='该问卷下的问题',default=1,on_delete=models.DO_NOTHING)
    question_A = models.CharField('A',max_length=30)
    question_B = models.CharField('B', max_length=30)
    question_C = models.CharField('C', max_length=30)
    question_D = models.CharField('D', max_length=30)
    question_E = models.CharField('E', max_length=30,null=True)
    question_F = models.CharField('F', max_length=30,null=True)
    question_G = models.CharField('G', max_length=30,null=True)
    question_H = models.CharField('H', max_length=30,null=True)
    question_I = models.CharField('I', max_length=30,null=True)
    question_J = models.CharField('J', max_length=30,null=True)
    question_K = models.CharField('K', max_length=30,null=True)

    def __str__(self):
        return self.caption



class Answer(models.Model):
    question = models.ForeignKey(to=Question,verbose_name='问题',on_delete=models.CASCADE)
    invest_user = models.ForeignKey(to=InvestigateUserInfo,verbose_name='调查用户',on_delete=models.SET_NULL,null=True)
    investigator = models.ForeignKey(to=Investigator,verbose_name='调查员',on_delete=models.SET_NULL,null=True)
    question_A = models.BooleanField(choices=((0,'N'),(1,'Y')),default=0)
    question_B = models.BooleanField(choices=((0,'N'),(1,'Y')),default=0)
    question_C = models.BooleanField(choices=((0,'N'),(1,'Y')),default=0)
    question_D = models.BooleanField(choices=((0,'N'),(1,'Y')),default=0)
    question_E = models.BooleanField(choices=((0,'N'),(1,'Y')),default=0)
    question_F = models.BooleanField(choices=((0,'N'),(1,'Y')),default=0)
    question_G = models.BooleanField(choices=((0,'N'),(1,'Y')),default=0)
    question_H = models.BooleanField(choices=((0,'N'),(1,'Y')),default=0)
    question_I = models.BooleanField(choices=((0,'N'),(1,'Y')),default=0)
    question_J = models.BooleanField(choices=((0,'N'),(1,'Y')),default=0)
    question_K = models.CharField(max_length=125,verbose_name='K. 其他',blank=True,null=True)




