from django import forms
from slider.models import Sliders 



class CreateSliderForm(forms.ModelForm):

	class Meta:
		model = Sliders
		fields = ['title', 'body', 'image', 'link']


class UpdateSliderPostForm(forms.ModelForm):

	class Meta:
		model = Sliders
		fields = ['title', 'body', 'image', 'link']

	def save(self, commit=True):
		slider_post = self.instance
		slider_post.title = self.cleaned_data['title']
		slider_post.link = self.cleaned_data['link']
		slider_post.body = self.cleaned_data['body']

		if self.cleaned_data['image']:
			slider_post.image = self.cleaned_data['image']

		if commit:
			slider_post.save()
		return slider_post