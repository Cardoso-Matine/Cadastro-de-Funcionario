from django.contrib import admin
from.models import Funcionario


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('name,title')
    


admin.site.register(Funcionario) #FuncionarioAdmin
