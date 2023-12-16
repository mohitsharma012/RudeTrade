# i have creted this file

from django.db import connection

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from userauth.models import rudeusers

from addtrade.models import usersData ,user_daily_pnl



def account(request):
    userid = request.session.get('userid')

    user_data = rudeusers.objects.filter(id = userid)
    for data in user_data:
        Fname = data.first_name
        Lname = data.last_name
        email = data.user_email
        currency = data.currency
        country = data.country

    para = {'pagename': 'Account','Fname':Fname,'Lname':Lname, 'email':email,'currency': currency, 'country':country }
    return render(request, 'account-settings.html',para)



def note(request):
    para = {'pagename': 'Note' }
    return render(request, 'note.html',para)

def updateuserdetails(request):
    userid = request.session.get('userid')
   
    if (request.method == "POST"):

        Fname = request.POST.get('Fname')
        Lname = request.POST.get('Lname')
        email = request.POST.get('email')
        currency = request.POST.get('currency')
        country = request.POST.get('country')

        update_user_details = rudeusers.objects.get(id= userid)

        update_user_details.first_name = Fname
        update_user_details.last_name = Lname
        update_user_details.user_email = email
        update_user_details.currency = currency
        update_user_details.country = country

        update_user_details.save()
        
    return redirect('account')




# def update_data_from_database():
#     # userid = request.session.get('userid')
#     cursor = connection.cursor()    


#     print("this function will print mohit")


def delete_all_trades(request):
    userid = request.session.get('userid')

    usersData.objects.filter(user_id_id = userid).delete()
    user_daily_pnl.objects.filter(user_id_id = userid).delete()



    return redirect("dashboard")