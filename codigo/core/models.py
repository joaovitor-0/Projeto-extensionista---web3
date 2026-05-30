from django.db import models


class Inscrito(models.Model):
    nome = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        max_length=100,
        unique=True
    )

    telefone = models.CharField(
        max_length=20,
        blank=True
    )

    data_inscricao = models.DateTimeField(
        auto_now_add=True
    )

    ativo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nome

class Atividade(models.Model):

    STATUS_CHOICES = [
        ('Aberta', 'Aberta'),
        ('Em andamento', 'Em andamento'),
        ('Encerrada', 'Encerrada')
    ]

    nome_atividade = models.CharField(
        max_length=100
    )

    descricao = models.TextField(
        blank=True
    )

    data_atividade = models.DateField(
        null=True,
        blank=True
    )

    local_atividade = models.CharField(
        max_length=100,
        blank=True
    )

    quantidade_vagas = models.IntegerField(
        null=True,
        blank=True
    )

    status_atividade = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    def __str__(self):
        return self.nome_atividade


class Participacao(models.Model):

    atividade = models.ForeignKey(
        Atividade,
        on_delete=models.CASCADE
    )

    voluntario = models.ForeignKey(
        Inscrito,
        on_delete=models.CASCADE
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        unique_together = ('atividade', 'voluntario')

        verbose_name = 'Voluntário'

        verbose_name_plural = 'Voluntários'

    def __str__(self):
        return f'{self.voluntario} - {self.atividade}'

class Transparencia(models.Model):
    TIPO_CHOICES = [
        ('Despesa', 'Despesa'),
        ('Arrecadação em dinheiro', 'Arrecadação em dinheiro'),
        ('Arrecadação de item', 'Arrecadação de item'),
    ]

    descricao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    data = models.DateField()
    exibir_no_site = models.BooleanField(default=True)

    def __str__(self):
        return self.descricao

class Newsletter(models.Model):
    nome = models.CharField(max_length=100)

    email = models.EmailField(max_length=100, unique=True)

    telefone = models.CharField(max_length=20, blank=True)

    cidade = models.CharField(max_length=100, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
