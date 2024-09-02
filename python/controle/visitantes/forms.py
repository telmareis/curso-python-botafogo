from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = (
            "nome_completo",
            "cpf",
            "data_nascimento",
            "numero_casa",
            "placa_veiculo",
        )

        criar_mensagens = {
            "nome_completo":{
                "required": "O nome completo é obrigatório"
            },
            "cpf": {
                "required": "O CPF é um campo obrigatório"
            },
            "data_nascimento":{
                "required": "A data é obrigatória",
                "invalid": "A data precisa ter o formato DD/MM/AAAA"
            },
            "numero_casa": {
                "required": "O número da casa é um campo obrigatório"
            },
        }
class AutorizaVisitanteForm(forms.ModelForm):
    morador_responsavel = forms.CharField(required=True)
    class Meta:
        model = Visitante
        fields = [
            "morador_responsavel"
        ]
        error_messages = {
            "morador_responsavel": {
                "required": "Informe o morador responsável"
            }
        }
        