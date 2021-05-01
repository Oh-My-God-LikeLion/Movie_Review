from .models import Content
from django import forms


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'score',
                  'release_date', 'genre', 'plot', 'review', ]
