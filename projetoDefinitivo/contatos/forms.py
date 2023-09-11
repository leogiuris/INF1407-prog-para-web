from django import forms
from contatos.models import Pessoa

class ContatoModel2Form(forms.ModelForm):
    
    nome = forms.CharField(
        label='Nome ',
        widget=forms.TextInput(attrs={'class':'w-auto form-control', 'placeholder':'nome'}),
    )
    idade = forms.IntegerField(
        label='Idade ',
        widget=forms.NumberInput(attrs={'class':'w-auto form-control', 'placeholder':'idade'}),
    )
    salario = forms.DecimalField(
        label='Salário ',
        widget=forms.NumberInput(attrs={'class':'w-auto form-control', 'placeholder':'salario'}),
    )
    email = forms.CharField(
        label='Email ',
        widget=forms.EmailInput(attrs={'class':'w-auto form-control', 'placeholder':'email'}),
    )
    telefone = forms.CharField(
        label='Telefone ',
        widget=forms.TextInput(attrs={'class':'w-auto form-control', 'placeholder':'telefone'}),
    )
    dtNasc = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Data de Nascimento  ',
        widget=forms.DateInput(attrs={'class':'w-auto form-control', 'placeholder':'dtNasc'}),
    )
    class Meta:
        model = Pessoa
        fields = '__all__'
        labels = {
            'nome': '',
            'idade': '',
            'salario': '',
            'email': '',
            'telefone': '',
            'dtNasc': '',
        }
        helper_texts = {
            'nome': '',
            'idade': '',
            'salario': '',
            'email': '',
            'telefone': '',
            'dtNasc': '',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':'nome'}),
            'idade': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'idade'}),
            'salario': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'salario'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}),
            'telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'telefone'}),
        }