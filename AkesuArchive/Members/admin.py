from django.contrib import admin
from .models import Subject, Topic, Note #GetClass

# Register your models here.

admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Note)
#admin.site.register(GetClass)