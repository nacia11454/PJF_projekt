from django.contrib import admin

# Register your models here.
from .models import Group, Plant, Care, User

admin.site.register(Group)
admin.site.register(Plant)
admin.site.register(Care)
admin.site.register(User)