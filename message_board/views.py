from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import Message


@login_required
def messagePageView(request):
	items = Message.objects.all().values_list('content', flat=True)

	return render(request, 'pages/message_board.html', {'items' : items})

@login_required
@csrf_exempt
def add(request):
    message = request.POST.get('content')
    new = Message(content=message)

    new.save()
    return redirect('../')

@login_required
def clear(request):
    Message.objects.all().delete()
    return redirect('../')