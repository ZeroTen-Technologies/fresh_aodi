from django import forms
from testimonials.models import Testimonials 



class CreateTestimonyForm(forms.ModelForm):

	class Meta:
		model = Testimonials
		fields = ['title', 'body', 'image']


class UpdateTestimonyPostForm(forms.ModelForm):

	class Meta:
		model = Testimonials
		fields = ['title', 'body', 'image']

	def save(self, commit=True):
		testimony_post = self.instance
		testimony_post.title = self.cleaned_data['title']
		testimony_post.body = self.cleaned_data['body']

		if self.cleaned_data['image']:
			testimony_post.image = self.cleaned_data['image']

		if commit:
			testimony_post.save()
		return testimony_post