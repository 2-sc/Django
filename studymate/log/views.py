from xml.dom import WrongDocumentErr
from django.shortcuts import render
from .models import Board
from user.models import UserProfile, User
from .forms import Boardform
# Create your views here.

def log(request):
    return render(request, 'log.html')

def boardList(request):
    pass

def boardWrite(request):
    if(request.method == 'POST'):
        contents = request.POST.get('contents', None)
        userid = request.session.get('user')
        user = User.objects.get(pk=userid)
        #username = user.username
        if contents:
            board = Board(
                contents = contents,
                writer = user
            )
            board.save()
        
    boards = Board.objects.all().order_by('-id')
    return render(request, 'log.html', {'boards': boards})