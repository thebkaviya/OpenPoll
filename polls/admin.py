from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = 'OpenPoll Admin'
admin.site.site_title = 'OpenPoll'

admin.site.register(Question)
admin.site.register(Choice)
