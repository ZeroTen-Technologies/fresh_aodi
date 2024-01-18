from django.urls import path
from testimonials.views import(
	create_testimonials_view,
	testimony_success_view,
	testimony_edit_success_view,
	detail_testimonials_view,
	edit_testimonials_view,
	testimonials_delete_view,
)

app_name = 'testimonials'


urlpatterns = [
	path('create/', create_testimonials_view, name="create"),
	path('success/', testimony_success_view, name="success"),
	path('edit_success/', testimony_edit_success_view, name="edit_success"),
	path('<slug>/', detail_testimonials_view, name="detail"),
	path('<slug>/edit', edit_testimonials_view, name="edit"),
	path('<id>/delete', testimonials_delete_view, name="delete"),
]

