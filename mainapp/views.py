from django.shortcuts import render
from django.http import JsonResponse
from .models import CompanyMetrc,Label,LabelCategory
import pandas as pd

# Create your views here.
def label_upload(request):
    if request.method =="POST":
        df = pd.read_csv(request.FILES['file'],delimiter=',')
        # print(df.columns)
        # print(df['first_name'])
        list_of_csv = [list(row) for row in df.values]
        for i in list_of_csv:
            temp = CompanyMetrc.objects.create()
            queryset_list = CompanyMetrc.objects.all()
            if i[0] != 'first_name':
                qs = queryset_list.filter(first_name__contains=i[0])
                if qs:#len(qs)>0:
                    continue
                else:
                    print('first_name',i[0])
                    temp.first_name = i[0]
            temp.last_name = i[1],
            print(temp.last_name)
            temp.email = i[2] 
            temp.save()      
    return render(request,'mainapp/index.html')

def csv_label_upload(request):
    if request.method =="POST":
        df = pd.read_csv(request.FILES['file'],delimiter=',')
        list_of_csv = [list(row) for row in df.values]
        for df_col in df.columns:
            qs = LabelCategory.objects.filter(title=df_col)
            if len(qs)>0:
                if df_col == qs[0].title:
                    for lvalue in df[df_col]:
                        duplicate = Label.objects.filter(title=lvalue)
                        if len(duplicate)>0:
                            continue
                        else:
                            Label.objects.create(
                            title=lvalue,
                            slug=lvalue,
                            category=LabelCategory.objects.filter(title=df_col)[0]
                            )
                else:
                    LabelCategory.objects.create(title=df_col,slug=df_col)
            else:
                LabelCategory.objects.create(title=df_col,slug=df_col)
    return render(request,'mainapp/label.html')


def csv_upload_temp(request):

    return render(request,'mainapp/label_ajax.html')


def csv_upload_ajax(request):
    if request.method =="POST":
        df = pd.read_csv(request.FILES['file'],delimiter=',')
        list_of_csv = [list(row) for row in df.values]
        for df_col in df.columns:
            qs = LabelCategory.objects.filter(title=df_col)
            if len(qs)>0:
                if df_col == qs[0].title:
                    for lvalue in df[df_col]:
                        duplicate = Label.objects.filter(title=lvalue)
                        if len(duplicate)>0:
                            continue
                        else:
                            Label.objects.create(
                            title=lvalue,
                            slug=lvalue,
                            category=LabelCategory.objects.filter(title=df_col)[0]
                            )
                else:
                    LabelCategory.objects.create(title=df_col,slug=df_col)
            else:
                LabelCategory.objects.create(title=df_col,slug=df_col)
    return JsonResponse({'msg':'Successfull uploaded.......'})

