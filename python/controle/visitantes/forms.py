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
