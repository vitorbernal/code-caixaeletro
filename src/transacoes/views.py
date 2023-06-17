import requests
from django.shortcuts import render
from django.views.generic import FormView
from .forms import DepositarForm, DebitarForm

# Create your views here.
class DepositarView(FormView):
    form_class = DepositarForm
    template_name = 'depositar.html'
    success_url = '/depositar/'

    def form_valid(self, form):
        cliente_id = form.cleaned_data['cliente']
        valor = form.cleaned_data['valor']

        url = f'http://127.0.0.1:8001/api/v1/clientes/{cliente_id}/depositar/'
        payload = {'valor': valor}

        resp = requests.put(url, data=payload)

        context_data = self.get_context_data()
        context_data['api_response'] = resp.json()
        context_data['cliente_enviado'] = cliente_id
        context_data['valor_enviado'] = valor
        return render(self.request, self.template_name, context_data)
    
class DebitarView(FormView):
    form_class = DebitarForm
    template_name = 'debitar.html'
    success_url = '/debitar/'

    def form_valid(self, form):
        cliente_id = form.cleaned_data['cliente']
        valor = form.cleaned_data['valor']

        url = f'http://127.0.0.1:8001/api/v1/clientes/{cliente_id}/debitar/'
        payload = {'valor': valor}

        resp = requests.put(url, data=payload)

        context_data = self.get_context_data()
        context_data['api_response'] = resp.json()
        context_data['cliente_enviado'] = cliente_id
        context_data['valor_enviado'] = valor
        return render(self.request, self.template_name, context_data)
