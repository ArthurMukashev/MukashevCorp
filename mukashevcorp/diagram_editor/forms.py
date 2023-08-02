from django import forms
from django.contrib.auth.models import Group

from .models import InformationSchema

SCHEMES = InformationSchema.objects.all()


class InformationSchemaForm(forms.ModelForm):
    linked = forms.ModelMultipleChoiceField(
        label='Связана с:',
        queryset=InformationSchema.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = InformationSchema
        exclude = ['author', 'linked', 'history']
    # name = forms.CharField(label='Название', max_length=255, required=True)
    # desc_short = forms.CharField(label='Краткое описание', max_length=255)
    # description = forms.CharField(label='Описание', widget=forms.Textarea)
    # linked = forms.TypedMultipleChoiceField(
    #     coerce=InformationSchema,
    #     choices=SCHEMES,
    #     widget=forms.CheckboxSelectMultiple
    # )

# class InformationSchemaForm(forms.Form):
#     name = forms.CharField('Название', max_length=255)
#     desc_short = forms.CharField('Краткое описание', max_length=255)
#     description = forms.Textarea('Описание')
#     linked = forms.CheckboxSelectMultiple(
#         queryset=InformationSchema.objects.all(),
#         required=False,
#         widget=forms.CheckboxSelectMultiple,
#         verbose_name='Связана с:'
#     )
#     permitted_groups = forms.CheckboxSelectMultiple(
#         queryset=Group.objects.all(),
#         required=True,
#         widget=forms.CheckboxSelectMultiple,
#         verbose_name='Доступна для:'
#     )
#
#     class Meta:
#         model = InformationSchema
