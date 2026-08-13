from django.db import models
from decimal import Decimal
from django.urls import reverse


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


class Banner(models.Model):
    titulo = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Título'
    )

    subtitulo = models.CharField(
        max_length=250,
        blank=True,
        verbose_name='Subtítulo'
    )

    imagem = models.ImageField(
        upload_to='banners/',
        verbose_name='Imagem'
    )

    link = models.URLField(
        max_length=500,
        blank=True,
        verbose_name='Link'
    )

    ordem = models.PositiveIntegerField(
        default=0,
        verbose_name='Ordem'
    )

    ativo = models.BooleanField(
        default=True,
        verbose_name='Ativo'
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['ordem', 'id']
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.titulo or f'Banner {self.id}'

class Campanha(models.Model):
    titulo = models.CharField(
        max_length=150,
        verbose_name='Título'
    )

    descricao = models.TextField(
        verbose_name='Descrição'
    )

    imagem = models.ImageField(
        upload_to='campanhas/',
        blank=True,
        null=True,
        verbose_name='Imagem'
    )

    meta = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Meta da campanha'
    )

    valor_arrecadado = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name='Valor alcançado'
    )

    texto_meta = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Descrição da meta',
        help_text='Exemplo: 50 quimonos, 100 cestas básicas ou R$ 5.000,00.'
    )

    link = models.URLField(
        blank=True,
        verbose_name='Link da campanha',
        help_text='Link opcional para doação, inscrição ou mais informações.'
    )

    texto_botao = models.CharField(
        max_length=50,
        blank=True,
        default='Saiba mais',
        verbose_name='Texto do botão'
    )

    ativa = models.BooleanField(
        default=True,
        verbose_name='Campanha ativa'
    )

    concluida = models.BooleanField(
        default=False,
        verbose_name='Campanha concluída'
    )

    ordem = models.PositiveIntegerField(
        default=0,
        verbose_name='Ordem de exibição'
    )

    data_inicio = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de início'
    )

    data_fim = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de encerramento'
    )

    criada_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizada_em = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Campanha'
        verbose_name_plural = 'Campanhas'
        ordering = ['ordem', '-criada_em']

    def __str__(self):
        return self.titulo

    @property
    def percentual(self):
        if not self.meta or self.meta <= Decimal('0'):
            return 0

        percentual = (
            self.valor_arrecadado / self.meta
        ) * Decimal('100')

        return min(round(percentual, 1), Decimal('100'))

    @property
    def percentual_real(self):
        if not self.meta or self.meta <= Decimal('0'):
            return 0

        percentual = (
            self.valor_arrecadado / self.meta
        ) * Decimal('100')

        return round(percentual, 1)

    def get_absolute_url(self):
        return reverse('funcionarios_campanhas')