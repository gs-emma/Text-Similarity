from django import forms 

# create a form that asks the user to input text 
class TextSubmission(forms.Form):
    text1 = forms.CharField(widget=forms.Textarea)
    text2 = forms.CharField(widget=forms.Textarea)