from django.contrib import admin
from order.models import UserCart,CartItem



@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ('user',)

