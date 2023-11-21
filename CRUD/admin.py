from django.contrib import admin
from website.models import Subscription, User


# Register your models here.
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('sub_name', 'sub_email')


class UserAdmin(admin.ModelAdmin):
    list_display = ('u_id', 'u_name', 'u_email', 'u_contact')


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(User, UserAdmin)
