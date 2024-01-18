from django import forms
from personal.models import Contact, Donation 



class CreateContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = ['fname', 'email', 'subject', 'message']

class DonationForm(forms.ModelForm):

	class Meta:
		model = Donation
		fields = ['full_name', 'email', 'item', 'item_title', 'item_num', 'currency', 'amount', 'body']



