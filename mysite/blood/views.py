from django.shortcuts import render
from .models import User

# Create your views here.

def badd(request):
    # =====新增的程式碼=====#
    if request.method == "POST":
        user_name = request.POST.get('user_name')  # 對應剛剛add.html 中的input name
        blood_high = request.POST.get('blood_high')
        blood_low = request.POST.get('blood_low')
        user = User(user_name=user_name, blood_high=blood_high, blood_low=blood_low)
        user.save()
        return render(request, 'badd.html', locals())
    return render(request, 'badd.html', locals())

def bdetail(request):
    list_user = User.objects.all()
    return render(request, 'bdetail.html', locals())