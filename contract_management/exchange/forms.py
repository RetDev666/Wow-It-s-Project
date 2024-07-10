# exchange/forms.py

from django import forms
from .models import Brokerage, Broker, Commodity, Contract

class BrokerageForm(forms.ModelForm):
    class Meta:
        model = Brokerage
        fields = '__all__'

class BrokerForm(forms.ModelForm):
    class Meta:
        model = Broker
        fields = '__all__'

class CommodityForm(forms.ModelForm):
    class Meta:
        model = Commodity
        fields = '__all__'

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
