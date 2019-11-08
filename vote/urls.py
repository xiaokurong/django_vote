from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'vote'

urlpatterns = [
    path('',views.vote_index,name='vote_index'),
    # path('login/',views.user_login,name='login'),
    path('questionnaire/',views.questionnaire,name='questionnaire'),
    path('investigator/',views.investigator,name='investigator'),
    path('history/',views.history,name='history'),
    path('question/',views.question,name='question'),
    path('investigateuser/',views.investigateuser,name='investigateuser'),
    path('other/',views.other,name='other'),


    # path('login/',auth_views.LoginView.as_view(),name='login'),
    # path('logout/',auth_views.LogoutView.as_view(),name='logout'),

]
