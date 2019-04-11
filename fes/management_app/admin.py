from django.contrib import admin

"""
    Created by Wenqiang Kuang
    Register models, such that in the django admin backend, corresponding models could be modified. 
"""
from .models import Client, Course, FesClass

admin.site.register(Client)
admin.site.register(Course)
admin.site.register(FesClass)
