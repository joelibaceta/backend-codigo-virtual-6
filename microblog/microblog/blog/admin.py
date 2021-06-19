from blog.models import Post, HashTag
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    pass

class HashtagAdmin(admin.ModelAdmin):

    HashTag

    pass


admin.site.register(Post, PostAdmin)
admin.site.register(HashTag, HashtagAdmin)