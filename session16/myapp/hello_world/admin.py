from hello_world.models import Gretting
from django.contrib import admin

# Register your models here.
class GreetingAdmin(admin.ModelAdmin):
    model = Gretting

admin.site.register(Gretting, GreetingAdmin)