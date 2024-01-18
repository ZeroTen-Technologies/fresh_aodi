from django import forms
from outreach.models import Outreaches 



class CreateOutreachForm(forms.ModelForm):

	class Meta:
		model = Outreaches
		fields = ['title', 'body', 'image']


class UpdateOutreachPostForm(forms.ModelForm):

	class Meta:
		model = Outreaches
		fields = ['title', 'body', 'image']

	def save(self, commit=True):
		outreach_post = self.instance
		outreach_post.title = self.cleaned_data['title']
		outreach_post.body = self.cleaned_data['body']

		if self.cleaned_data['image']:
			outreach_post.image = self.cleaned_data['image']

		if commit:
			outreach_post.save()
		return outreach_post