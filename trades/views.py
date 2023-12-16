from django.shortcuts import render
from addtrade.models import usersData


# Create your views here.
def trades(request):
    
    userid = request.session.get('userid')
    get_trades = usersData.objects.filter(user_id=userid).order_by('-entry_datetime')

    return render(request, 'trades.html',{'get_trades': get_trades})
