from django.shortcuts import redirect, render, HttpResponse
from ..models import User, Branch
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
            user = User.objects.get(username = username)

        except:
            return HttpResponse("user doesn't exists")

        if not pbkdf2_sha256.verify(password, user.password):
            return HttpResponse("wrong password")

        request.session['start'] = True
        request.session['username'] = username
        request.session['auth-level'] = user.auth_level
        request.session['top-level'] = user.top_level

        request.session.save()

        if user.top_level:
            return redirect('/top-level/home/')
        else:
            return redirect('/')

@never_cache
def logout(request):
    lg(request)
    return redirect('/login/')

def register(request):
    return render(request, 'registration.html', {'branches': Branch.objects.all()})

def registerprocess(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        position = request.POST['position']
        branch = request.POST['branch']

        first_name = request.POST['fname']
        last_name = request.POST['lname']

        if User.objects.filter(username=username).exists():
            return HttpResponse('Username already taken')

        user = User()

        user.username = username
        user.password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)
        user.branch = Branch.objects.get(pk=branch)
        if position == "Head":
            user.auth_level = 'Head'
        else:
            user.auth_level = 'Empoloyee'

        user.first_name = first_name
        user.last_name = last_name
        user.position = position

        user.save()

        return redirect('/')