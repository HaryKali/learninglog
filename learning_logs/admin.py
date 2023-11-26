from django.contrib import admin
from learning_logs.models import Topic,Entry,Entry_md
# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Entry_md)
