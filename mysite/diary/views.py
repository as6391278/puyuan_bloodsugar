from django.shortcuts import render
from .models import User

# Create your views here.

def dadd(request):
    # =====新增的程式碼=====#
    if request.method == "POST":
        date = request.POST.get('date')  # 對應剛剛add.html 中的input name
        diary = request.POST.get('diary')
        user = User(date=date,diary=diary)
        user.save()
        return render(request, 'dadd.html', locals())
    return render(request, 'dadd.html', locals())

def ddetail(request):
    list_user = User.objects.all()
    return render(request, 'ddetail.html', locals())
def ddelete(request):                  #刪除資料
    # if id!=None:
    # if request.method == "POST":  #如果是以POST的分是才處理
    date = request.POST.get('date')  #取得表單輸入的編號
    try:
        unit = User.objects.get(date=date)  #取得id欄位的資料
        unit.delete()
    except:
        pass
   # print(type(date))
    # try:
    # unit = User.objects.all()  #取得id欄位的資料
    # print(unit)
    # for R in enumerate(unit):
    #     print(R)
    #     print(date)
    #     print(type(R))
    #     print(type(date))
    #     if (str(R)==date):
    #         print(1)
    #         unit1=R.objects.get(date=date)
    #         unit1.delete()  
    #         print(type(unit))
    #         print(unit)
    
    #                   #刪除資料
    return render(request,"ddelete.html",locals())
