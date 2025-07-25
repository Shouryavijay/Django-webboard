from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Topic, Post

def home(request):
    boards = Board.objects.all()
    return render(request, 'board/home.html', {'boards': boards})

def topic_list(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    topics = Topic.objects.filter(board=board)
    return render(request, 'board/topic_list.html', {'board': board, 'topics': topics})

def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']
        topic = Topic.objects.create(board=board, title=title)
        Post.objects.create(topic=topic, message=message)
        return redirect('topic_list', board_id=board.id)
    return render(request, 'board/new_topic.html', {'board': board})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    posts = Post.objects.filter(topic=topic)
    return render(request, 'board/topic_detail.html', {'topic': topic, 'posts': posts})

def reply_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == 'POST':
        message = request.POST['message']
        Post.objects.create(topic=topic, message=message)
        return redirect('topic_detail', topic_id=topic.id)
    return render(request, 'board/reply.html', {'topic': topic})
