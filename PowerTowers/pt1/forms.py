from django import forms
from pt1.models import QueryForm


class FormName(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.IntegerField()
    comments = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = QueryForm
        fields = '__all__'
