from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import cryptocompare as cryptcomp

# Create your views here.
class miningcalc(View):
    queryset = ''
    hash_rate = 12
    consumed_power = 10
    costKWh = 8
    block_reward = 12.5
    block_time = 600
    network_hash_rate = 1.8410989266292908E9
    template_name = 'index.html'
    net_profit = 0
    def get(self,request,*args,**kwargs):
        print(request.GET)
        requests = request.GET
        if request.GET:
            print("is not empty")
            self.hash_rate = float(request.GET.get('hashRate'))
            self.consumed_power = float(request.GET.get('power'))
            self.costKWh = float(request.GET.get('cost'))
            self.coin_price = cryptcomp.get_price('BTC',curr='USD')['BTC']['USD']
            self.net_profit = ((self.hash_rate / self.network_hash_rate) * (self.block_reward * self.block_time) * self.coin_price) - (self.costKWh * (self.consumed_power / 1000))
            print("NET PROFIT: {} with hashRate after AJAX: {}".format(self.net_profit,self.hash_rate))
            return JsonResponse({
                "net_profit": self.net_profit
            })
        else:
            self.coin_price = cryptcomp.get_price('BTC',curr='USD')['BTC']['USD']
            self.net_profit = ((self.hash_rate / self.network_hash_rate) * (self.block_reward * self.block_time) * self.coin_price) - (self.costKWh * (self.consumed_power / 1000))
            print("NET PROFIT: {} with hasRate befor AJAX: {}".format(self.net_profit,self.hash_rate))
            print("is empty")
        context = {
            'net_profit': self.net_profit,
            'hashRate': self.hash_rate,
            'power': self.consumed_power,
            'cost': self.costKWh
        }
        return render(request,self.template_name, {'context':context})
    def post(self,request,*args,**kwargs):
        self.hash_rate = float(request.POST.get('hashRate'))
        self.consumed_power = float(request.POST.get('power'))
        self.costKWh = float(request.POST.get('cost'))
        self.coin_price = cryptcomp.get_price('BTC',curr="USD")['BTC']['USD']
        self.net_profit = ((self.hash_rate / self.network_hash_rate) * (self.block_reward * self.block_time) * self.coin_price) - (self.costKWh * (self.consumed_power / 1000))
        print("NET PROFIT: {}".format(self.net_profit))
        context = {
            'net_profit': self.net_profit,
            'hashRate': self.hash_rate,
            'power': self.consumed_power,
            'cost': self.costKWh
        }
        return render(request,self.template_name, {'context':context})