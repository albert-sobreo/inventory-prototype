from django.shortcuts import redirect, render, HttpResponse
from ..models import Login, User
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import logout as lg
from django.views.decorators.cache import never_cache

# Create your views here.
def login(request):
    if request.session.is_empty():
        return render(request, 'login.html')
    else:
        return redirect('/')

def loginprocess(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            login = Login.objects.get(username = username)

        except:
            return HttpResponse("user doesn't exists")

        if not pbkdf2_sha256.verify(password, login.password):
            return HttpResponse("wrong password")

        request.session['start'] = True
        request.session['username'] = username
        request.session['auth-level'] = login.auth_level

        request.session.save()

        return redirect('/')

@never_cache
def logout(request):
    lg(request)
    return redirect('/login/')

def register(request):
    return render(request, 'registration.html')

def registerprocess(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        position = request.POST['position']

        first_name = request.POST['fname']
        last_name = request.POST['lname']

        if Login.objects.filter(username=username).exists():
            return HttpResponse('Username already taken')

        login = Login()
        user = User()

        login.username = username
        login.password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)
        if position == "b0ss":
            login.auth_level = 'b0ss'
        else:
            login.auth_level = 'not b0ss'

        login.save()

        user.first_name = first_name
        user.last_name = last_name
        user.position = position
        user.login = login

        user.save()

        return redirect('/')