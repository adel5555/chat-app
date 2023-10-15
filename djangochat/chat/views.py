from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Room, Message

@login_required(login_url=reverse_lazy('login-user'))
def rooms(request):
	rooms = Room.objects.all()
	return render(request,'Rooms.html',{'rooms':rooms})

@login_required(login_url=reverse_lazy('login-user'))
def room(request,slug):
	room_name=Room.objects.get(slug=slug).name
	messages=Message.objects.filter(room=Room.objects.get(slug=slug))

	return render(request,'Room.html',{"room_name":room_name,"slug":slug,'messages':messages})