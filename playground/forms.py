from django import forms

class TaskNamesForm(forms.Form):
    task1 = forms.CharField()
    task2 = forms.CharField()
    task3 = forms.CharField()
    task4 = forms.CharField()
    task5 = forms.CharField()
