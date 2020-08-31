from django.contrib import admin

# Register your models here.
from .models import Post, Comment, info,education,work,skills,hobby



admin.site.register(Post)
admin.site.register(Comment)

admin.site.register(info)
admin.site.register(education)
admin.site.register(work)
admin.site.register(skills)
admin.site.register(hobby)