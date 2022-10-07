from django.contrib import admin
# from tally.app1.models import Ledger_vouchers
from app1.models import Ledger_vouchers
from app1.models import tally_ledger
from app1.models import tally_group
from app1.models import StockGroup, stock_item
from app1.models import Stockcategory
from app1.models import voucherlist
# Register your models here.
admin.site.register(Ledger_vouchers)
admin.site.register(tally_ledger)
admin.site.register(tally_group)
admin.site.register(StockGroup)
admin.site.register(stock_item)
admin.site.register(Stockcategory)
admin.site.register(voucherlist)