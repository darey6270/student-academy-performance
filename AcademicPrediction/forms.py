from django import forms


class GradeForm(forms.Form):
    score1 = forms.IntegerField()
    score2 = forms.IntegerField()
    score3 = forms.IntegerField()
    score4 = forms.IntegerField()
    score5 = forms.IntegerField()
    score6 = forms.IntegerField()
    score7 = forms.IntegerField()
    score8 = forms.IntegerField()
    score9 = forms.IntegerField()
    score10 = forms.IntegerField()
    point1 = forms.FloatField()
    point2 = forms.FloatField()
    point3 = forms.FloatField()
    point4 = forms.FloatField()
    point5 = forms.FloatField()
    point6 = forms.FloatField()
    point7 = forms.FloatField()
    point8 = forms.FloatField()
    point9 = forms.FloatField()
    point10 = forms.FloatField()
