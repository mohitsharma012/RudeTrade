from django.contrib import admin

# Register your models here.

from .models import usersData
admin.site.register(usersData)



from .models import user_daily_pnl
admin.site.register(user_daily_pnl)
