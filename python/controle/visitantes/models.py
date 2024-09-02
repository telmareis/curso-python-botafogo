from django.db import models

STATUS_VISITANTE = [
    ("AGUARDANDO", "Aguardando autorização"),
    ("EM_VISITA", "Em visita"),
    ("FINALIZADO", "Visita finalizada"),
]

class Visitante(models.Model):
    status = models.CharField(
        verbose_name = "Status",
        max_length = 10,
        choices = STATUS_VISITANTE,
        default="AGUARDANDO"
    )

    registrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.PROTECT,
    )
    nome_completo = models.CharField(
        verbose_name="Nome Completo",
        max_length=150,
    )
    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )
    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        auto_now_add=False,
        auto_now=False,
    )
    numero_casa = models.PositiveSmallIntegerField(
        verbose_name="Número da casa a ser visitada",
    )
    placa_veiculo = models.CharField(
        verbose_name="Placa do Veículo",
        max_length=7,
        blank=True,
        null=True,
    )
    horario_chegada = models.DateTimeField(
        verbose_name="Horário de Chegada na Portaria",
        auto_now_add=True,
    )
    horario_saida = models.DateTimeField(
        verbose_name="Horário de saída do condomínio",
        auto_now=False,
        blank=True,
        null=True,
    )
    horario_autorizacao = models.DateTimeField(
        verbose_name="Horário de Autorização de Entrada",
        auto_now=False,
        blank=True,
        null=True,
    )
    morador_responsavel = models.CharField(
        verbose_name="Nome do morador responsável por autorizar a entrada",
        max_length=50,
        blank=True,
    )

    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida

        return "Horário de saída não registrado"
    
    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao

        return "Horário da autorização de entrada"

    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel

        return "Morador responsável"

    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo

        return "Placa do veículo"


    class Meta:
        verbose_name="Visitante"
        verbose_name_plural="Visitantes"
        db_table="visitante"
        
    def __str__(self):
        return self.nome_completo    
    
    