from django.shortcuts import render
from django.views import View
import cryptocompare as cryptcomp

# Create your views here.
class miningcalc(View):
    queryset = ''
    template_name = 'index.html'
    net_profit = 0
    def get(self,request,*args,**kwargs):
        context = {
            'net_profit': self.net_profit
        }
        return render(request,self.template_name, {'context':context})
    def post(self,request,*args,**kwargs):
        self.hash_rate = float(request.POST.get('hash-rate'))
        self.consumed_power = float(request.POST.get('power'))
        self.costKWh = float(request.POST.get('cost'))
        self.coin_price = cryptcomp.get_price('BTC',curr="USD")['BTC']['USD']
        self.net_profit = self.hash_rate * self.coin_price - self.costKWh * self.consumed_power
        print("NET PROFIT: {}".format(self.net_profit))
        context = {
            'net_profit': self.net_profit
        }
        return render(request,self.template_name, {'context':context})
