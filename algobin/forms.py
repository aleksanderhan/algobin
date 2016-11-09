from django import forms


class AlgorithmForm(forms.Form):
    name = forms.CharField(
    	label='*Name', 
    	max_length=50, 
    	required=True)

    description = forms.CharField(
    	label='Short description', 
    	max_length=600,
    	widget=forms.Textarea(attrs = {'cols': '150', 'rows': '4'}))

    code = forms.CharField(
    	label='*Algorithm', 
    	required=True,
    	widget=forms.Textarea(attrs = {'cols': '150', 'rows': '30'}))