from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_lenght=100)
    assunto = forms.CharField(label='Assunto', max_lenght=100)
    mensagem = forms.CharField('Mensagem',widget=forms.Textarea())