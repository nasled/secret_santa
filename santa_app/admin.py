from django.contrib import admin
from django.contrib.auth.models import User

from .models import Pair
from .tasks import send_emails


def make_pair(modeladmin, request, queryset):
    queryset.update(mailed=True)

    for values in queryset.values_list():
        UserOne = User.objects.get(id=values[1])
        UserTwo = User.objects.get(id=values[2])
        send_emails(UserOne, UserTwo)

make_pair.short_description = "Send Email"


class PairAdmin(admin.ModelAdmin):
    list_display = ['userOne', 'userTwo', 'mailed']
    ordering = ['mailed']
    actions = [make_pair]

admin.site.register(Pair, PairAdmin)