from django.urls import path
from trustees.views import(
	create_trustee_view,
	trustee_success_view,
	trustee_edit_success_view,
	detail_trustee_view,
	trustee_comment_exist_view,
	edit_trustee_view,
	trustee_delete_view,
)

app_name = 'trustees'


urlpatterns = [
	path('create/', create_trustee_view, name="create"),
	path('success/', trustee_success_view, name="success"),
	path('trustee_comment_exist/', trustee_comment_exist_view, name="trustee_comment_exist"),
	path('edit_success/', trustee_edit_success_view, name="edit_success"),
	path('<slug>/', detail_trustee_view, name="detail"),
	path('<id>/edit', edit_trustee_view, name="edit"),
	path('<id>/delete', trustee_delete_view, name="delete"),
]

