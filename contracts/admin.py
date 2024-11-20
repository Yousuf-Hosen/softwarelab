from django.contrib import admin
from .models import Contract

# Register your models here.
class ContractAdmin(admin.ModelAdmin):
    list_display=('id','name','listing','email','contract_date')
    list_display_links=('id','name')
    search_fields=('name','email','listing')
    list_per_page=25
    

admin.site.register(Contract,ContractAdmin)
