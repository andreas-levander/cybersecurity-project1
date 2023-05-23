from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from message_board_v1.controllers import users
from .models import Message_v1 as Message


def homePage(request):
    return render(request, 'pages/index.html')

def registerPage(request):
    if request.method == "GET":
        return render(request, 'registration/register.html')
    else:
        print(request.POST)
        users.better_create_user(request.POST.get('username'), request.POST.get('password'))
        return render(request, 'registration/register.html', {"notif": "Successfully registered user"} )
    
def loginPage(request):
     notif = ""
     if request.method == "POST":
          if users.better_check_password(request.POST.get('username'), request.POST.get('password')):
               request.session["user"] = request.POST.get('username')
               return redirect("../../")
          notif = "Incorrect username of password"
     return render(request, 'registration/login_v1.html', {'notif': notif})

def messagePageView(request):
	items = Message.objects.all().values_list('content', flat=True)

	return render(request, 'pages/message_board.html', {'items' : items})

@csrf_exempt
def add(request):
    message = request.POST.get('content')
    new = Message(content=message)

    new.save()
    return redirect('../')


def clear(request):
    Message.objects.all().delete()
    return redirect('../')