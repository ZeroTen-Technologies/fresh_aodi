from django.urls import path
from blog.views import(
	create_blog_view,
	blog_success_view,
	blog_edit_success_view,
	detail_blog_view,
	blog_comment_exist_view,
	edit_blog_view,
	blog_delete_view,
)

app_name = 'blog'


urlpatterns = [
	path('create/', create_blog_view, name="create"),
	path('success/', blog_success_view, name="success"),
	path('blog_comment_exist/', blog_comment_exist_view, name="blog_comment_exist"),
	path('edit_success/', blog_edit_success_view, name="edit_success"),
	path('<slug>/', detail_blog_view, name="detail"),
	path('<slug>/edit', edit_blog_view, name="edit"),
	path('<id>/delete', blog_delete_view, name="delete"),
]

