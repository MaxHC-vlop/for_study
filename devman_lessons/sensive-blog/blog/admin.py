from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdminModel(admin.ModelAdmin):
    raw_id_fields = ['author', 'likes', 'tags']


@admin.register(Tag)
class TagAdminModel(admin.ModelAdmin):
    raw_id_fields = ['posts']


@admin.register(Comment)
class CommentAdminModel(admin.ModelAdmin):
    raw_id_fields = ['author', 'post']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'author',
            'post'
        )