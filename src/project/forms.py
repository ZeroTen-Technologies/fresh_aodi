from django import forms
from project.models import Projects, ProjectCategory



class CreateProjectForm(forms.ModelForm):

	class Meta:
		model = Projects
		fields = ['title', 'body', 'image', 'amount', 'currency', 'category']


class UpdateProjectPostForm(forms.ModelForm):

	class Meta:
		model = Projects
		fields = ['title', 'body', 'image', 'amount', 'currency', 'category']

	def save(self, commit=True):
		project_post = self.instance
		project_post.title = self.cleaned_data['title']
		project_post.currency = self.cleaned_data['currency']
		project_post.amount = self.cleaned_data['amount']
		project_post.category = self.cleaned_data['category']
		project_post.body = self.cleaned_data['body']

		if self.cleaned_data['image']:
			project_post.image = self.cleaned_data['image']

		if commit:
			project_post.save()
		return project_post


class CreateProjectCategoryForm(forms.ModelForm):

	class Meta:
		model = ProjectCategory
		fields = ['title', 'body']