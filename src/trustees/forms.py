from django import forms
from trustees.models import Bio 



class CreateTrusteeForm(forms.ModelForm):

	class Meta:
		model = Bio
		fields = ['title', 'body', 'governing_board', 'founding_trustees', 'appointed_trustees', 'amb_membership', 'project_facilitator', 'volunteer', 'associate_membership', 'image']


class UpdateTrusteePostForm(forms.ModelForm):

	class Meta:
		model = Bio
		fields = ['title', 'body', 'image']

	def save(self, commit=True):
		bio_post = self.instance
		bio_post.title = self.cleaned_data['title']
		bio_post.body = self.cleaned_data['body']

		if self.cleaned_data['image']:
			bio_post.image = self.cleaned_data['image']

		if commit:
			bio_post.save()
		return bio_post