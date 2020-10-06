from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login as log
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from .form import *





def write(sing) :

    TextFile = open('usermanage.txt', 'a', encoding='UTF-8')
    for i in sing:

        if i == sing[2]:
            TextFile.write('says: \n')

        TextFile.write(str(i) + '\n')

    TextFile.write('\n' + '\n'+ '###########################' + '\n'+'\n')
    TextFile.close()
    
        
        







def home(request):
    contactform = contactForm
    content = {
        'form' : contactform
    }

    # a is contact us form credentials
    a = []
    if request.method == 'POST':
        a.append(request.POST.get('name'))
        a.append(request.POST.get('email'))
        a.append(str(request.POST.get('msg')))
        print(a)
        write(a)

    return render(request, 'index.html', content)





# make a model for new user (CLASS)!
user_model = get_user_model()

def register(request):
    register_form = RegisterForm(request.POST or None)
    content = {
        'form': register_form
    }

    print(request.POST.get('password'))
    print(request.POST.get('password2'))

    if register_form.is_valid():
        print(register_form.cleaned_data)
        
        unam = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        pasW = register_form.cleaned_data.get('password')
        newUser = User.objects.create_user(username=unam, email=email, password=pasW)
        print(f'we have a new user called ##{newUser}##')

        content['form'] = RegisterForm()

        return redirect('/login')

    return render(request, 'auth/register.html', content)





# ==============
# login page
# ===============
def login(request):


    login_form = LoginForm(request.POST or None)
    content = {
        'login':login_form,

    }

    if login_form.is_valid():
        
        unam = login_form.cleaned_data.get('username')
        pasW = login_form.cleaned_data.get('password')
        user = authenticate(request, username=unam, password=pasW)
        print(f' user %%{login_form.cleaned_data.get("username")}%% is trying to log in')
        myName = request.user
        print(f'is user """" {myName} """"logged in : {request.user.is_authenticated}')

        if user is not None:
            log(request, user)
            content['login'] = LoginForm()
            return redirect('/')

        else:
            print(f'user {login_form.cleaned_data.get("username")} returns %%None%%')
       
    return render(request, 'auth/login.html', content)
# ==============
# login page ends
# ===============