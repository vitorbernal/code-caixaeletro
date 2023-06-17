from django import forms

class DepositarForm(forms.Form):
    cliente = forms.IntegerField(label='ID do cliente', required=True)
    valor = forms.DecimalField(label='valor', required=True)

class DebitarForm(DepositarForm):
    pass