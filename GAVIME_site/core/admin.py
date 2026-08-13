from django.contrib import admin

from .models import Inscrito
from .models import Atividade
from .models import Participacao
from .models import Banner


admin.site.register(Inscrito)
admin.site.register(Atividade)
admin.site.register(Participacao)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
        'ordem',
        'ativo',
        'data_cadastro',
    ]

    list_editable = [
        'ordem',
        'ativo',
    ]

    list_filter = [
        'ativo',
    ]

    search_fields = [
        'titulo',
        'subtitulo',
    ]

    ordering = [
        'ordem',
        'id',
    ]

