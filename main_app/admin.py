import imp
from django.contrib import admin
from main_app.models import Tech, Review
# Register your models here.
admin.site.register(Tech)
admin.site.register(Review)