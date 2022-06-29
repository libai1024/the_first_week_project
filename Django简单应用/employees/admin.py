from django.contrib import admin

# Register your models here.
from employees.models import Staff
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):

    list_display = ['name','age','tel']
    ordering = ['name']

    actions = ['logging_output']

    def logging_output(self, request,queryset):

        print("日志输出")

    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST['action'] == 'logging_output':
            if not request.POST.getlist(ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                for u in Staff.objects.all():
                    post.update({ACTION_CHECKBOX_NAME: str(u.id)})
                request._set_post(post)
        return super(StaffAdmin, self).changelist_view(request, extra_context)

    logging_output.short_description = '日志输出'
    logging_output.type = 'success'
    def __str__(self):
        return "员工"


