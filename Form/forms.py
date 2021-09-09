from django import forms
class ResumeData(forms.Form):
    name=forms.CharField()
    file=forms.FileField()