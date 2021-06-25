from django.contrib import admin
from exam.models import Question, Option

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    pass

class OptionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)