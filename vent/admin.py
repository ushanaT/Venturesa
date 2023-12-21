from django.contrib import admin
from .models import Accounts,Investment_plans, Activated_plans,Withdrawals , Deposit_request,Admin_account_no, Coin_rate


# Register your models here.

admin.site.register(Accounts)
admin.site.register(Investment_plans)
admin.site.register(Activated_plans)
admin.site.register(Withdrawals)
admin.site.register(Deposit_request)
admin.site.register(Coin_rate)
admin.site.register(Admin_account_no)