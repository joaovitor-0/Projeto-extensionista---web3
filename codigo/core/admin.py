from django.contrib import admin

from .models import Inscrito
from .models import Atividade
from .models import Participacao


admin.site.register(Inscrito)
admin.site.register(Atividade)
admin.site.register(Participacao)