# exchange/admin.py

from django.contrib import admin
from .models import Brokerage, Broker, Commodity, Contract

admin.site.register(Brokerage)
admin.site.register(Broker)
admin.site.register(Commodity)
admin.site.register(Contract)
