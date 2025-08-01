from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Topic, Post
from .forms import NewTopicForm, ReplyForm, PostForm
from django.contrib.auth.models import User

def home(request):
    boards = Board.objects.all()
    return render(request, 'board/home.html', {'boards': boards})

def topic_list(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    topics = board.topics.all()
    return render(request, 'board/topic_list.html', {'board': board, 'topics': topics})

def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            return redirect('board:topic_list', board_id=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'board/new_topic.html', {'board': board, 'form': form})

def topic_detail(request, board_id, topic_id):
    board = get_object_or_404(Board, pk=board_id)
    topic = get_object_or_404(Topic, pk=topic_id, board=board)
    return render(request, 'board/topic_detail.html', {'board' : board, 'topic': topic})

def reply_topic(request, board_id, topic_id):
    board = get_object_or_404(Board, pk=board_id)
    topic = get_object_or_404(Topic, pk=topic_id, board=board)
    
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('board:topic_detail', 
                         board_id=board.pk, 
                         topic_id=topic.pk)
    else:
        form = ReplyForm()
    
    return render(request, 'board/reply_topic.html', {
        'board': board,
        'topic': topic,
        'form': form
    })