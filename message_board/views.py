from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Message



def messagePageView(request):

	items = Message.objects.all().values_list('content', flat=True)
    
	print(items)

	return render(request, 'pages/message_board.html', {'items' : items})

def add(request):
    message = request.POST.get('content')
    new = Message(content=message)

    new.save()
    return redirect('../')