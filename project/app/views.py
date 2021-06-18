from django.http import HttpResponse
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
    global CrossTab
    CrossTab= pd.crosstab(data1,data2,margins=True)
    print(CrossTab)
    CrossTab.to_excel("Pivot_Data.xlsx")
    b= CrossTab.to_html()

    table = open("C:/Users/Inderjeet/PycharmProjects/Assignment5/project/app/templates/output1.html", "w")
    table.write(b)
    table.close()

    table = open("C:/Users/Inderjeet/PycharmProjects/Assignment5/project/app/templates/output1.html", "a")
    table.write(r'<button onclick ="window.location.href=`/down_file`">Download File</button>')
    table.close()

    table = open("C:/Users/Inderjeet/PycharmProjects/Assignment5/project/app/templates/output1.html", "a")
    table.write(r'<button onclick ="window.location.href=`/transpose`">Transpose</button>')
    table.close()
    return render(request, "output1.html", {"string":b})

def down_file(request):
    with open('Pivot_Data.xlsx', 'rb') as model_excel:
        result = model_excel.read()
    response = HttpResponse(result)
    response['Content-Disposition'] = 'attachment; filename=Pivot_Table.xlsx'
    return response

def transpose(request):
    transpose=CrossTab.transpose()
    print(transpose)
    transpose.to_excel("Pivot_Data_Transpose.xlsx")
    c = transpose.to_html()

    table = open("C:/Users/Inderjeet/PycharmProjects/Assignment5/project/app/templates/output2.html", "w")
    table.write(c)
    table.close()

    table = open("C:/Users/Inderjeet/PycharmProjects/Assignment5/project/app/templates/output2.html", "a")
    table.write(r'<button onclick ="window.location.href=`/downfile_transpose`">Download Transpose File</button>')
    table.close()

    return render(request, "output2.html", {"string": c})

def downfile_transpose(request):
    with open('Pivot_Data_Transpose.xlsx', 'rb') as model_excel:
        result = model_excel.read()
    response = HttpResponse(result)
    response['Content-Disposition'] = 'attachment; filename=Pivot_Table_Transpose.xlsx'
    return response




