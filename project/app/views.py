from django.shortcuts import render
from django.views.generic import TemplateView
import pandas as pd
import numpy as np

class MainPage(TemplateView):
    template_name = 'home.html'

def mainpage(request):

    file = pd.read_excel("Data Records.xlsx")
    # print(file)
    return render(request, "display.html", {"string": file})

def output(request):

    file = pd.read_excel("Data Records.xlsx")
    # print(file)
    var1 = request.POST['dropdown1']
    # print(var1)
    var2 = request.POST['dropdown2']
    # print(var2)
    data1=file[var1]
    data2=file[var2]
    CrossTab= pd.crosstab(data1,data2,margins=True)
    print(CrossTab)
    b= CrossTab.to_html()

    table = open("C:/Users/Inderjeet/PycharmProjects/Assignment5/project/app/templates/output1.html", "w")
    table.write(b)
    table.close()

    return render(request, "output1.html", {"string":b})










