from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'] #make pub date come before question text
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date']}),
    ]  
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

""" Anytime you need to change the admin options for a model, 
create a model admin class and pass it as a second argument to admin.site.register()"""
admin.site.register(Question, QuestionAdmin)