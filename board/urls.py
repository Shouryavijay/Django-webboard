from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.home, name='home'),  # Homepage that lists all boards
    path('boards/<int:board_id>/', views.topic_list, name='topic_list'),  # List of topics in a board
    path('boards/<int:board_id>/new/', views.new_topic, name='new_topic'),  # Form to create a new topic
    path('boards/<int:board_id>/topics/<int:topic_id>/', views.topic_detail, name='topic_detail'),  # Show posts in a topic
    path('boards/<int:board_id>/topics/<int:topic_id>/reply/', views.reply_topic, name='reply_topic'),  # Form to reply to a topic
]
