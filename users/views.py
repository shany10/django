from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from users.EmailBackEnd import EmailBackend

# Create your views here.
def home(request):
    template = loader.get_template('core/home.html')
    return HttpResponse(template.render())

def login(request):
    return render(request, 'core/login.html')

def inscription(request):
    """ if request.method == 'POST':
        form = MyUsersForm(request.POST)
        if form.is_valid():
           
            form.save()
            return render(
                request, 
                'core/inscription.html', 
                {'form': MyUsersForm(), 'success': True}
            )        
    else:
        form = MyUsersForm() """
    return render(request, 'core/inscription.html')

def isLogin(request): 
    if request.method!='POST':
        return HttpResponse('No!')
    else:
        user=EmailBackend.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user != None:
            login(request)
            return HttpResponseRedirect('/homeAdmin')
        else:
            return HttpResponse('Invalid Login')
        
def GetUserDetails(request):
    if request.user != None:
        return HttpResponse('User : ' + request.user.email + 'usertype : ' + request.user.user_type)
    else:
        return HttpResponse('Login to start')
    
def Logout(request):
    logout(request)
    return HttpResponse('/')