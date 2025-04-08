from django.shortcuts import render
from pyexpat.errors import messages

from .models import ChatRoom, ChatMessage


# Create your views here.
def index(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chatapp/index.html', {"rooms":rooms})

def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)[0:30]
    return render(request, 'chatapp/room.html', {"chatroom": chatroom, "messages":messages})