from django.contrib import admin
from blog.models import Blogs, BlogComment, BlogCommentReply

# Register your models here.
admin.site.register(Blogs)
admin.site.register(BlogComment)
admin.site.register(BlogCommentReply)
