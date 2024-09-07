from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
from django.contrib import messages


from userauth.models import rudeusers



def index(request):


    return render(request, 'index.html')

def signupaction(request):
    
    if (request.method =='POST'):
        Fname = request.POST.get('Fname')
        Lname = request.POST.get('Lname')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        Cpwd = request.POST.get('Cpwd')

        check_user_exist = rudeusers.objects.filter(user_email = email)

        if (len(check_user_exist) > 0):
            print("user already")
            messages.success(request, 'Email is already in use choose another one!')

        else:
            
            if (pwd == Cpwd):
                save_user = rudeusers(first_name = Fname, last_name = Lname, user_email =email, user_pass = pwd)
                save_user.save()
                messages.success(request, 'Account created sucessfully!')


            else:
                messages.success(request, 'Password is not Matching!')

    return redirect('index_name')

def loginaction(request):
    if (request.method == "POST"):

        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        check_user = rudeusers.objects.filter(user_email= email, user_pass = pwd)

        if (len(check_user) == 1 ):
            userid = rudeusers.objects.filter(user_email = email)
            for i in userid:
                request.session['userid'] = i.id
                

            return redirect('dashboard')
        else:
            messages.success(request, 'Incorrect Email And Password!')


    return redirect('index_name')


