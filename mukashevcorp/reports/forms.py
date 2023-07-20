from django import forms


class ReportFragmentForm(forms.Form):
    report_year = forms.ChoiceField(widget=forms.Select, label="Год отчета",
                                    choices=[(2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)])
    report_text = forms.CharField(widget=forms.Textarea, label="Текст фрагмента")
