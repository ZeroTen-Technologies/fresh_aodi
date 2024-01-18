from django.urls import path
from outreach.views import(
	create_outreach_view,
	outreach_success_view,
	outreach_edit_success_view,
	detail_outreach_view,
	edit_outreach_view,
	outreach_delete_view,
)

app_name = 'outreach'


urlpatterns = [
	path('create/', create_outreach_view, name="create"),
	path('success/', outreach_success_view, name="success"),
	path('edit_success/', outreach_edit_success_view, name="edit_success"),
	path('<slug>/', detail_outreach_view, name="detail"),
	path('<slug>/edit', edit_outreach_view, name="edit"),
	path('<id>/delete', outreach_delete_view, name="delete"),
]
