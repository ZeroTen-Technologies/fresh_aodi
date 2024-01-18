import re  
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from project.models import Projects
from outreach.models import Outreaches
from personal.models import Subscribe
from personal.models import Contact, Donation
from slider.models import Sliders
from testimonials.models import Testimonials
from personal.forms import CreateContactForm, DonationForm

# Create your views here.
context = {}
def home_view(request):
	# deleting session variable from subscribe
	if 'name_newsletter' in request.session:
		del request.session['name_newsletter']

	if 'email_newsletter' in request.session:
		del request.session['email_newsletter']

	if 'wrong_email' in request.session:
		del request.session['wrong_email']

	projects = Projects.objects.all().order_by('-id')[:6]
	outreaches = Outreaches.objects.all().order_by('-id')[:6]
	sliders = Sliders.objects.all().order_by('-id')
	testimonials = Testimonials.objects.all().order_by('id')
	


	context['projects'] = projects
	context['outreaches'] = outreaches
	context['sliders'] = sliders
	context['testimonials'] = testimonials
	return render(request, 'personal/new_home.html', context)

def about_view(request):
	return render(request, 'personal/new_about.html', {})

def aims_and_obj_view(request):
	return render(request, 'personal/new_aims_and_obj.html', {})

def our_constitution_view(request):
	return render(request, 'personal/new_our_constitution.html', {})


def form_test_view(request):
	fname = request.POST.get('fname')
	email = request.POST.get('email')

	if fname == 'None':
		context['fname'] = ''
	elif email == 'None':
		context['email'] = ''
	else:
		context['fname'] = fname
		context['email'] = email
	return render(request, 'personal/form_test.html', context)


def subscribe_view(request):
	fname = request.POST.get('fname')
	email = request.POST.get('email')


	# name_regex = '^(([A-Za-z]+[,.]?[ ]?|[a-z]+['-]?)+)$'

	email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 

	if(re.search(email_regex,email)):
		if Subscribe.objects.filter(email=email).exists():
			request.session['name_newsletter'] = fname
			request.session['email_newsletter'] = email
			return redirect('already_subscribed')
		else:
			subscribe = Subscribe(name=fname, email=email)
			subscribe.save()
			subscribe_id = get_object_or_404(Subscribe, id=subscribe.id)
	else:
		request.session['name_newsletter'] = fname
		request.session['wrong_email'] = email
		return redirect('already_subscribed')

	# find_records = Subscribe.objects.filter(email=email).exists
	# check_records = Subscribe.objects.filter(email=fname).exists()
	

	context['hello'] = subscribe_id
	return render(request, 'personal/subscribe.html', context)

def subscribe_warning_view(request):
	return render(request, 'personal/subscribe_warning.html', {})

def contact_view(request):
	# fname = request.POST.get('fname')
	# email = request.POST.get('email')
	# subject = request.POST.get('subject')
	# message = request.POST.get('message')

	# contacted = Contact(fname=fname, email=email, subject=subject, message=message)
	# contacted.save()
	# contacted_id = get_object_or_404(Contact, id=contacted.id)
	# context['hi'] = contacted_id
	# contact = Contact(fname=fname, email=email, subject=subject, message=message)
	# # contact.save()
	# contact_id = get_object_or_404(Contact, id=contact.id)
	
	# context['hello'] = contact_id

	form = CreateContactForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		obj_id = get_object_or_404(Contact, id=obj.id)
		context['hi'] = obj_id
		context['success_message'] = "Your message was sent successfully. We will get back to you as soon as possible. Thanks"
		form = CreateContactForm()

	context['form'] = form
	return render(request, 'personal/contact.html', context)

def membership_view(request):
	return render(request, 'personal/membership.html', context)

def governing_board_view(request):
	return render(request, 'personal/governing_board.html', context)

def founding_trustees_view(request):
	return render(request, 'personal/new_founding_trustees.html', context)

def appointed_trustees_view(request):
	return render(request, 'personal/appointed_trustees.html', context)

def ambassadors_view(request):
	return render(request, 'personal/ambassadors.html', context)

def associate_membership_view(request):
	return render(request, 'personal/associate_membership.html', context)

def project_facilitators_view(request):
	return render(request, 'personal/project_facilitators.html', context)

def volunteers_view(request):
	return render(request, 'personal/volunteers.html', context)

def donate_view(request):
	return render(request, 'personal/donate.html', context)

def pay_view(request):
	return render(request, 'personal/pay.html', context)

def process_pay_view(request):
	full_name = request.POST.get('full_name')
	email = request.POST.get('email')
	item = request.POST.get('item')
	item_title = request.POST.get('item_title')
	item_num = request.POST.get('item_num')
	currency = request.POST.get('currency')
	amount = request.POST.get('amount')
	body = request.POST.get('body')

	donate = Donation(full_name=full_name, email=email, item=item, item_title=item_title, item_num=item_num, currency=currency, amount=amount, body=body)
	donate.save()

	context = {
		"full_name": full_name,
		"email": email,
		"amount": amount,
		"currency": currency,
	}

	return render(request, 'personal/process_pay.html', context)

def testpage_view(request):
	return render(request, 'personal/testpage.html', context)

def finaltest_view(request):
	return render(request, 'personal/finaltest.html', context)


