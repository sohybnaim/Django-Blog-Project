from django.contrib import admin
from dataclasses import field
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fieldsets=(
        ["User Information",{'fields':["first_name","last_name","age"]}],
    )
    list_display=("first_name","last_name","age","email","phone_number","country")
    list_filter=["first_name","age","country"]
    search_fields=["first_name","age","country"]


admin.site.register(User,UserAdmin) 


# Register your models here.
