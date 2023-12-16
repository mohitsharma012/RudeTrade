from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
from addtrade.models import usersData, user_daily_pnl
from django.utils import timezone
from datetime import datetime


def addtrade(request):
    count = 0
    para = {"pagename": "New Trade", "count": count}
    return render(request, "addtrade.html", para)


def addtrade_multiple(request):
    para = {"pagename": "New Trades"}
    return render(request, "addtrade-multiple.html", para)


def one_more(request):
    count = count + 1
    para = {"pagename": "New Trade", "count": count}
    return render(request, "addtrade.html", para)


def newtrade(request):
    cursor = connection.cursor()
    aware_datetime = timezone.make_aware(datetime(2023, 5, 27, 15, 27))

    userid = request.session.get("userid")

    action = request.POST.get("action")
    market = request.POST.get("market")
    symbol = request.POST.get("symbol")
    quantity = float(request.POST.get("quantity"))
    Endt = request.POST.get("Entrydt")
    Exdt = request.POST.get("Exdt")
    EnP = float(request.POST.get("EnP"))
    ExP = float(request.POST.get("ExP"))
    EnR = request.POST.get("EnR")
    folowsetup = request.POST.get("folowsetup")
    note = request.POST.get("note")
    trade_rating = request.POST.get("rating")

    if action == "BUY":
        pnl = (ExP - EnP) * quantity
    elif action == "SELL":
        pnl = (EnP - ExP) * quantity

    make_new_trade = usersData(
        user_id_id=userid,
        action=action,
        market=market,
        symbol=symbol,
        quantity=quantity,
        entry_datetime=Endt,
        exit_datetime=Exdt,
        entry_price=EnP,
        exit_price=ExP,
        entry_reason=EnR,
        follow_setup=folowsetup,
        trade_note=note,
        pnl=pnl,
        trade_rating=trade_rating,
    )
    make_new_trade.save()

    Endt = datetime.strptime(Endt, "%Y-%m-%dT%H:%M")
    Endt_date = Endt.date()

    PNLS = user_daily_pnl.objects.filter(entry_datetime=Endt_date, user_id=userid)
    count = PNLS.count()

    if count != 0:
        for i in PNLS:
            pnl = pnl + i.daily_pnl

        update_day_pnl = user_daily_pnl.objects.get(
            user_id_id=userid,
            entry_datetime=Endt_date,
        )
        update_day_pnl.daily_pnl = pnl

        update_day_pnl.save()
    else:
        update_day_pnl = user_daily_pnl(
            user_id_id=userid, entry_datetime=Endt_date, daily_pnl=pnl
        )
        update_day_pnl.save()

    return redirect("dashboard")


from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from openpyxl import load_workbook
import csv


def upload_excel(request):
    userid = request.session.get("userid")

    if request.method == "POST" and "data_file" in request.FILES:
        uploaded_file = request.FILES["data_file"]
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension == "csv":
            decoded_file = uploaded_file.read().decode("utf-8")
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=",")
            next(csv_data)

            # Process the uploaded Excel file
            for row in csv_data:
                Endt, Exdt, action, quantity, symbol, market, EnP, ExP, pnl = row
                # Convert EnP and ExP to floats
                EnP = float(EnP)
                ExP = float(ExP)
                pnl = float(pnl)
                quantity = float(quantity)
                if pnl == "":
                    pnl = 0
                    if action == "BUY" or "buy":
                        pnl = (ExP - EnP) * quantity
                    elif action == "SELL" or "sell":
                        pnl = (EnP - ExP) * quantity

                make_new_trade = usersData(
                    user_id_id=userid,
                    action=action,
                    market=market,
                    symbol=symbol,
                    quantity=quantity,
                    entry_datetime=Endt,
                    exit_datetime=Exdt,
                    entry_price=EnP,
                    exit_price=ExP,
                    entry_reason="",
                    follow_setup="no",
                    trade_note="this is note",
                    pnl=pnl,
                    trade_rating=0,
                )
                make_new_trade.save()

                Endt = datetime.strptime(Endt, "%Y-%m-%dT%H:%M:%S.%f")
                Endt_date = Endt.date()

                PNLS = user_daily_pnl.objects.filter(
                    entry_datetime=Endt_date, user_id=userid
                )
                count = PNLS.count()

                if count != 0:
                    for i in PNLS:
                        print(i.daily_pnl)
                        pnl = pnl + i.daily_pnl
                    update_day_pnl = user_daily_pnl.objects.get(
                        user_id_id=userid,
                        entry_datetime=Endt_date,
                    )
                    update_day_pnl.daily_pnl = pnl

                    update_day_pnl.save()
                else:
                    print("mohit")
                    update_day_pnl = user_daily_pnl(
                        user_id_id=userid, entry_datetime=Endt_date, daily_pnl=pnl
                    )
                    update_day_pnl.save()

    return redirect("dashboard")
