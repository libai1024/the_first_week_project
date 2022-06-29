from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect,reverse

# Create your views here.
from django.views import View

from app01.forms import StaffForm, LoginForm
from employees.models import Staff
from app01.log import log, cal_runtime


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    @log
    @cal_runtime
    def post(self, request):
        login_form = LoginForm(request.POST)
        try:
            if login_form.is_valid():
                user_name = request.POST.get("username", "")
                pass_word = request.POST.get("password", "")
                user = authenticate(username=user_name, password=pass_word)
                if user is not None:
                    login(request, user)
                    return redirect(reverse('list'))
                else:
                    return render(request, "login.html", {"msg": u"用户名或者密码错误!"})
            else:
                return render(request, "login.html", {"login_form": login_form})
        except:
            return redirect(reverse('login'))
@log
@cal_runtime
def list(request):
    staff = Staff.objects.all()
    return render(request,"list.html",{"staff":staff})


@log
@cal_runtime
def add(request):
    clean_errors={}
    if request.method == "GET":
        form = StaffForm()
        return render(request, "change.html", {"form": form})
    else:
        form = StaffForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Staff.objects.create(**data)
            return redirect(reverse('list'))
        else:
            clean_errors = form.errors.get("__all__")
            return render(request, "change.html", {"form": form, "clean_errors": clean_errors})
@log
@cal_runtime
def delete(request,id):
    staff = Staff.objects.filter(id=id).first()
    staff.delete()
    return redirect(reverse('list'))

@log
@cal_runtime
def change(request,id):

    if request.method == "GET":
        staff = Staff.objects.filter(id=id).first()
        if staff:
            form = StaffForm(instance=staff)
        else:
            form = StaffForm()
        return render(request, "change.html", {"form": form})
    else:
        form = StaffForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Staff.objects.filter(id=id).update(**data)
            return redirect(reverse('list'))
        else:
            clean_errors = form.errors.get("__all__")
        return render(request, "change.html", {"form": form, "clean_errors": clean_errors})
