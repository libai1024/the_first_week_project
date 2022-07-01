import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from employees.models import Staff,MyUser

from django import forms


class StaffForm(ModelForm):
    class Meta:
        model= Staff
        fields = "__all__"
        exclude = None
    # def clean_name(self):  # 局部钩子
    #     val = self.cleaned_data.get("name")
    #     if Staff.objects.filter(name=val):
    #         raise ValidationError("员工已存在！")
    #     else:
    #         return val

    def clean_tel(self):
        val = self.cleaned_data.get("tel")
        patter = "(?<!\d)(1\d{10})(?!\d)"
        res_phone = re.compile(patter).findall(val)
        if res_phone:
            return val
        else:
            raise ValidationError("电话输入有误，请重试。")



class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)