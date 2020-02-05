from django.shortcuts import render

from .models import User

# Create your views here.

def fadd(request):
    # =====新增的程式碼=====#
    if request.method == "POST":
        user_name = request.POST.get('user_name')  # 對應剛剛add.html 中的input name
        user = User(user_name=user_name)
        user.save()
        return render(request, 'fadd.html', locals())
    return render(request, 'fadd.html', locals())

def fdetail(request):
    list_user = User.objects.all()
    return render(request, 'fdetail.html', locals())
def fdelete(request):                  #刪除資料
    print(request)
    # if id!=None:
    # if request.method == "POST":  #如果是以POST的分是才處理
    user_name = request.POST.get('user_name')  #取得表單輸入的編號
    print(user_name)
    try:
        unit = User.objects.get(user_name=user_name)  #取得id欄位的資料
        unit.delete()                      #刪除資料
        # return redirect('/fdelete.html/')
    except:
    #     message = "讀取錯誤!"
        pass
    return render(request,"fdelete.html",locals())
