from django import forms
from django.contrib.auth.models import Group

from .models import InformationSchema

SCHEMES = (InformationSchema.objects.all())


class InformationSchemaForm(forms.Form):
    name = forms.CharField('Название', max_length=255)
    desc_short = forms.CharField('Краткое описание', max_length=255)
    description = forms.Textarea('Описание')
    linked = forms.CheckboxSelectMultiple(
        queryset=InformationSchema.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        verbose_name='Связана с:'
    )
    permitted_groups = forms.CheckboxSelectMultiple(
        queryset=Group.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple,
        verbose_name='Доступна для:'
    )

    class Meta:
        model = InformationSchema
