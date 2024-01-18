from django.urls import path
from project.views import(
	create_project_view,
	create_project_category_view,
	project_success_view,
	project_edit_success_view,
	detail_project_view,
	all_project_in_cat,
	edit_project_view,
	project_delete_view,
)

app_name = 'project'


urlpatterns = [
	path('create/', create_project_view, name="create"),
	path('createprocat/', create_project_category_view, name="createprocat"),
	path('success/', project_success_view, name="success"),
	path('edit_success/', project_edit_success_view, name="edit_success"),
	path('<slug>/', detail_project_view, name="detail"),
	path('cat/<slug>/', all_project_in_cat, name="detail_cat"),
	path('<slug>/edit', edit_project_view, name="edit"),
	path('<id>/delete', project_delete_view, name="delete"),
]
