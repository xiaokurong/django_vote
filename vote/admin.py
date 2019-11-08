from django.contrib import admin
from .models import Investigator,InvestigateUserInfo,QuestionNaire,Question,Answer


# Register your models here.
admin.site.register(InvestigateUserInfo)
admin.site.register(Investigator)
admin.site.register(Question)
admin.site.register(QuestionNaire)
admin.site.register(Answer)
