from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:board_id>/', views.topic_list, name='topic_list'),
    path('boards/<int:board_id>/new/', views.new_topic, name='new_topic'),
    path('topics/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('topics/<int:topic_id>/reply/', views.reply_topic, name='reply_topic'),
]
