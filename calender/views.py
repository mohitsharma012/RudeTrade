from django.shortcuts import render
from datetime import datetime ,timedelta,date
from addtrade.models import user_daily_pnl,usersData
from json import dumps


def calender(request):
    userid = request.session.get('userid')

    dataDictionary = [] 
    PNLS = user_daily_pnl.objects.filter(user_id=userid)
    
    for pnl_record in PNLS:
        datePNL = {}
        datePNL["date"] = pnl_record.entry_datetime.strftime('%Y-%m-%d')  # Convert date to string
        datePNL["profit"] = pnl_record.daily_pnl
        dataDictionary.append(datePNL)

    dataJSON = dumps(dataDictionary)
    print(dataJSON)

    para = {'pagename': 'Calender', 'data': dataJSON }
    return render(request, 'calender.html',para)


def get_trades_for_date(request, date):
    userid = request.session.get('userid')

    trades = usersData.objects.filter(entry_datetime__date=date,user_id=userid)
    return render(request, 'task_popup.html', {'trades': trades})