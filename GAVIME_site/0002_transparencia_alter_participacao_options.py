from django import forms
from .models import Banner
from .models import Campanha


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner

        fields = [
            'imagem',
            'titulo',
            'subtitulo',
            'link',
            'ordem',
            'ativo',
        ]

        widgets = {
            'imagem': forms.ClearableFileInput(
                attrs={
                    'class': 'campoArquivo',
                    'accept': 'image/jpeg,image/png,image/webp',
                }
            ),

            'titulo': forms.TextInput(
                attrs={
                    'class': 'campoFormulario',
                    'placeholder': 'Título do banner',
                }
            ),

            'subtitulo': forms.TextInput(
                attrs={
                    'class': 'campoFormulario',
                    'placeholder': 'Texto complementar',
                }
            ),

            'link': forms.URLInput(
                attrs={
                    'class': 'campoFormulario',
                    'placeholder': 'https://exemplo.com.br',
                }
            ),

            'ordem': forms.NumberInput(
                attrs={
                    'class': 'campoFormulario',
                    'min': 0,
                }
            ),

            'ativo': forms.CheckboxInput(
                attrs={
                    'class': 'campoCheckbox',
                }
            ),
        }

    def clean_imagem(self):
        imagem = self.cleaned_data.get('imagem')

        if not imagem:
            return imagem

        tipo = getattr(imagem, 'content_type', None)

        tipos_permitidos = [
            'image/jpeg',
            'image/png',
            'image/webp',
        ]

        if tipo and tipo not in tipos_permitidos:
            raise forms.ValidationError(
                'Envie uma imagem JPG, PNG ou WEBP.'
            )

        tamanho_maximo = 8 * 1024 * 1024

        if hasattr(imagem, 'size') and imagem.size > tamanho_maximo:
            raise forms.ValidationError(
                'A imagem deve ter no máximo 8 MB.'
            )

        return imagem

class CampanhaForm(forms.ModelForm):

    class Meta:
        model = Campanha

        fields = [
            'titulo',
            'descricao',
            'imagem',
            'meta',
            'valor_arrecadado',
            'texto_meta',
            'link',
            'texto_botao',
            'ativa',
            'concluida',
            'ordem',
            'data_inicio',
            'data_fim',
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Exemplo: Apadrinhe um quimono'
            }),

            'descricao': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': (
                    'Explique o objetivo da campanha e como as pessoas '
                    'podem contribuir.'
                )
            }),

            'meta': forms.NumberInput(attrs={
                'min': '0.01',
                'step': '0.01',
                'placeholder': '0,00'
            }),

            'valor_arrecadado': forms.NumberInput(attrs={
                'min': '0',
                'step': '0.01',
                'placeholder': '0,00'
            }),

            'texto_meta': forms.TextInput(attrs={
                'placeholder': 'Exemplo: Meta de 50 quimonos'
            }),

            'link': forms.URLInput(attrs={
                'placeholder': 'https://'
            }),

            'texto_botao': forms.TextInput(attrs={
                'placeholder': 'Saiba mais'
            }),

            'ordem': forms.NumberInput(attrs={
                'min': '0'
            }),

            'data_inicio': forms.DateInput(attrs={
                'type': 'date'
            }),

            'data_fim': forms.DateInput(attrs={
                'type': 'date'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        meta = cleaned_data.get('meta')
        valor_arrecadado = cleaned_data.get('valor_arrecadado')
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')

        if meta is not None and meta <= 0:
            self.add_error(
                'meta',
                'A meta precisa ser maior que zero.'
            )

        if valor_arrecadado is not None and valor_arrecadado < 0:
            self.add_error(
                'valor_arrecadado',
                'O valor alcançado não pode ser negativo.'
            )

        if data_inicio and data_fim and data_fim < data_inicio:
            self.add_error(
                'data_fim',
                'A data de encerramento não pode ser anterior à data de início.'
            )

        return cleaned_data