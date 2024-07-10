# exchange/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Brokerage, Broker, Commodity, Contract
from .forms import BrokerageForm, BrokerForm, CommodityForm, ContractForm


def index(request):
    brokerages = Brokerage.objects.all()
    brokers = Broker.objects.all()
    commodities = Commodity.objects.all()
    contracts = Contract.objects.all()
    context = {
        'brokerages': brokerages,
        'brokers': brokers,
        'commodities': commodities,
        'contracts': contracts
    }
    return render(request, 'exchange/index.html', context)


@login_required
def brokerage_create(request):
    if request.method == 'POST':
        form = BrokerageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BrokerageForm()
    return render(request, 'exchange/form.html', {'form': form})


@login_required
def brokerage_update(request, pk):
    brokerage = get_object_or_404(Brokerage, pk=pk)
    if request.method == 'POST':
        form = BrokerageForm(request.POST, instance=brokerage)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BrokerageForm(instance=brokerage)

