from django.shortcuts import render
from addtrade.models import usersData ,user_daily_pnl
from userauth.models import rudeusers
from django.utils import timezone
import calendar
from datetime import datetime ,timedelta



def dashboard(request):

    userid = request.session.get('userid')
    current_date = datetime.today().date()


    userinfo =  rudeusers.objects.filter(id = userid)

    # daily_pnl_data = usersData.objects.filter(entry_datetime__date=current_date , user_id = userid)
    daily_pnl_data = user_daily_pnl.objects.filter(entry_datetime=current_date , user_id = userid)
    monthly_pnl_data = user_daily_pnl.objects.filter(entry_datetime__month=current_date.month, user_id=userid)
    net_pnl_data = user_daily_pnl.objects.filter(user_id=userid)
    total_wins_data = usersData.objects.filter(user_id=userid, pnl__gte=0)
    total_loss_data = usersData.objects.filter(user_id=userid , pnl__lt=0 )
    daily_pnl =0
    monthly_pnl = 0
    net_pnl = 0
    total_wins = 0
    total_loss = 0
    neg_daily_pnl = 0
    neg_monthly_pnl = 0
    neg_net_pnl = 0

    for pnls in daily_pnl_data:
        daily_pnl = pnls.daily_pnl
        daily_pnl  = round(daily_pnl,2)
        if(daily_pnl<0):
            neg_daily_pnl = -daily_pnl

    for pnls in monthly_pnl_data:
        monthly_pnl = monthly_pnl + pnls.daily_pnl
        monthly_pnl = round(monthly_pnl,2)
        if (monthly_pnl < 0):
            neg_monthly_pnl = -monthly_pnl

    for pnls in net_pnl_data:
        net_pnl = net_pnl + pnls.daily_pnl
        net_pnl = round(net_pnl,2)
        if (net_pnl < 0):
            neg_net_pnl = -net_pnl

    for wins in total_wins_data:
        total_wins += 1 
    for losses in total_loss_data:
        total_loss += 1
    for info in userinfo:
        currency_symbol = info.currency
    
    if (currency_symbol == "USD"):
        currency_symbol = "$"
    elif(currency_symbol == "INR"):
        currency_symbol = " INR"
    

    # this code is for monthly and weakly graps values
    today = datetime.now().date()

    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)


    weekly_pnl_list = []

    for i in range(7):
        day_pnl = 0
        data = usersData.objects.filter(user_id_id = userid, entry_datetime__date = start_of_week +timedelta(days=i))
        for j in data:
            date = j.entry_datetime
            day_pnl = day_pnl + j.pnl
        weekly_pnl_list.append(day_pnl)
    

    current_month = datetime.now().month
    days_in_current_month = calendar.monthrange(datetime.now().year, current_month)[1]
    current_month_start = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0).date()

    current_month_name = timezone.now().strftime('%B %Y')


    monthly_pnl_list = []
    monthly_date_list =[]

    for i in range(days_in_current_month):
        monthly_pnl_graph = 0
        data = usersData.objects.filter(user_id_id = userid, entry_datetime__date = current_month_start +timedelta(days=i))
        dates = current_month_start + timedelta(days = i)
        for j in data:
            monthly_pnl_graph = monthly_pnl_graph + j.pnl
        monthly_pnl_list.append(monthly_pnl_graph)
        monthly_date_list.append(dates)
    

    

    dashboard_data = {'pagename': "Dashboard", 'daily_pnl': daily_pnl,'monthly_pnl':monthly_pnl,'net_pnl':net_pnl,'total_wins':total_wins,'total_loss':total_loss, 'currency_symbol': currency_symbol, 'neg_daily_pnl': neg_daily_pnl ,'neg_monthly_pnl': neg_monthly_pnl, 'neg_net_pnl':neg_net_pnl,'weekly_pnl_list':weekly_pnl_list, 'monthly_pnl_list':monthly_pnl_list,'monthly_date_list':monthly_date_list,'current_month_name':current_month_name }
    return render(request, 'dashboard.html',dashboard_data)





