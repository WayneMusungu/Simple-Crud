
from django.shortcuts import render, redirect
from . models import Room
from .forms import RoomForm

# Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'main/home.html',context )


def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'main/room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        '''
        Create a variable that takes in POST request and returns value of a particular item
        '''
        # wayne = request.POST.get('name')
        # print(wayne)
        # OR
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'main/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context ={'form':form}
    return render (request, 'main/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    
    return render(request, 'main/delete.html', {'obj':room} )

