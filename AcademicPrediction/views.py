from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import GradeForm
import random
# Create your views here.
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


class AboutWebsite(TemplateView):
    template_name = "AcademicPrediction/about.html"


class ContactWebsite(TemplateView):
    template_name = "AcademicPrediction/contact.html"


def PredictionPage(request):
    y_pred = ''
    predictForm = GradeForm()
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            # score
            score1 = form.cleaned_data['score1']
            score2 = form.cleaned_data['score2']
            score3 = form.cleaned_data['score3']
            score4 = form.cleaned_data['score4']
            score5 = form.cleaned_data['score5']
            score6 = form.cleaned_data['score6']
            score7 = form.cleaned_data['score7']
            score8 = form.cleaned_data['score8']
            score9 = form.cleaned_data['score9']
            score10 = form.cleaned_data['score10']
            # grade
            cpoint1 = form.cleaned_data['point1']
            cpoint2 = form.cleaned_data['point2']
            cpoint3 = form.cleaned_data['point3']
            cpoint4 = form.cleaned_data['point4']
            cpoint5 = form.cleaned_data['point5']
            cpoint6 = form.cleaned_data['point6']
            cpoint7 = form.cleaned_data['point7']
            cpoint8 = form.cleaned_data['point8']
            cpoint9 = form.cleaned_data['point9']
            cpoint10 = form.cleaned_data['point10']

            sum_score = int(score1) + int(score2) + int(score3) + int(score4) + int(score5) + int(score6) + int(
                score7) + int(score8) + int(score9) + int(score10)
            sum_point = float(cpoint1) + float(cpoint2) + float(cpoint3) + float(cpoint4) + float(cpoint5) + float(
                cpoint6) + float(cpoint7) + float(cpoint8) + float(cpoint9) + float(cpoint10)
            a = np.array([sum_score, sum_point])
            # X = pd.DataFrame(a)
            X = a.reshape(1, -1)
            X_scaler = StandardScaler().fit(X)
            # X = X.transpose(X)
            X_scaler_s = X_scaler.transform(X)
            model = load_model("AcademicPrediction/SAP_model.h5")
            pred = model.predict(X_scaler_s)
            class_names = ['pass', 'lower_credit', 'upper_credit', 'distiction']
            random.shuffle(class_names)
            #[[0.00101546 0.98764914 0.00398455 0.00735078]]

            y_pred = class_names[np.argmax(pred)]
            remark = ''
            if y_pred == 'pass':
                remark = "Your report shows you often struggle to focus in class, which harms your ability to engage well with class activities and assignments.Be sure to ask for assistance. You need to listen to directions more attentively during lessons. Working on these problem areas every night would help improve your learning outcomes."
            if y_pred == 'lower_credit':
                remark = "You need to improve your cooperation in group settings. Ensure to accept a share of the work when participating in a group assignment. You would benefit from showing a greater desire to contribute ideas in class. Work on voicing feelings and emotions and listening to others."
            if y_pred == 'upper_credit':
                remark = "Very Good. You are encouraged to demonstrate a more responsible attitude and behavior in the classroom. You are determined and with some motivation, you can easily grow your numbers. Most of the people fall under the same category so you have a lot of competition to beat.Your developmental skills are strong but your analytical skills still needs to be up to the mark"
            if y_pred == 'distiction':
                remark = "Keep it up! Your report demonstrates a willing and conscientious effort in your daily work.”Your CGPA is among the highest and very few students are able to achieve this feat. Now you need to emphasize your projects and have some real life technical experience by doing some internships. You can also try to improve your social interaction and make connections"

            return render(request, "AcademicPrediction/results.html",
                          {"prediction_text": y_pred, "remark": remark})

            # [0.22175686 0.28321356 0.23812833 0.25690123]
            # [0.22175686 0.28321356 0.23812833 0.25690123]

        else:
            print(form.errors)
    else:
        predictForm = GradeForm()
    return render(request, "AcademicPrediction/predict.html",
                  {"form": predictForm})


class HomeWebsite(TemplateView):
    template_name = "AcademicPrediction/index.html"
