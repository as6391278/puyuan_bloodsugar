from django.shortcuts import render
from .models import User

# Create your views here.

def add(request):
    # =====新增的程式碼=====#
    if request.method == "POST":
        user_name = request.POST.get('user_name')  # 對應剛剛add.html 中的input name
        user_img = request.FILES.get('user_image')
        introduce = request.FILES.get('introduce')
        user = User(user_name=user_name, user_image=user_img, introduce=introduce)
        user.save()
        return render(request, 'add.html', locals())
    return render(request, 'add.html', locals())

def detail(request):
    list_user = User.objects.all()
    return render(request, 'detail.html', locals())