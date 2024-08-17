from django.contrib import admin
from .models import profile, Transactions
from django.contrib.auth.models import User, Group


admin.site.unregister(User) 
admin.site.unregister(Group) 

class transaction(admin.StackedInline):
    model = Transactions
class profileinline(admin.StackedInline):
    model = profile
class adminmodel(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [profileinline] 
# Register your models here.

admin.site.register(User, adminmodel)
admin.site.register(Transactions)
# admin.site.register(profile)
