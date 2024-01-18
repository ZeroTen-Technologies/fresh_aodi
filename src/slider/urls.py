from django.urls import path
from slider.views import(
	create_slider_view,
	slider_success_view,
	slider_edit_success_view,
	detail_slider_view,
	edit_slider_view,
	slider_delete_view,
)

app_name = 'slider'


urlpatterns = [
	path('create/', create_slider_view, name="create"),
	path('success/', slider_success_view, name="success"),
	path('edit_success/', slider_edit_success_view, name="edit_success"),
	path('<slug>/', detail_slider_view, name="detail"),
	path('<slug>/edit', edit_slider_view, name="edit"),
	path('<id>/delete', slider_delete_view, name="delete"),
]

