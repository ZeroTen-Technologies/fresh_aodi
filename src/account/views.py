from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from blog.models import Blogs
from project.models import Projects
from outreach.models import Outreaches
from slider.models import Sliders
from testimonials.models import Testimonials
from personal.models import Contact, Subscribe, Donation
from account.models import Account
from trustees.models import Bio


# Create your views here.
context = {}
def login_view(request):

	user = request.user
	if user.is_authenticated:
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect('home')

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form
	return render(request, 'account/login.html', context)




def signup_view(request):
	user = request.user
	if user.is_authenticated:
		return redirect('home')

	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form
	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/signup.html', context)


def forgot_password_view(request):
	return render(request, 'account/forgot-password.html', context)

def dashboard_view(request):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	total_num_of_blogs = Blogs.objects.all().count()
	total_num_of_projects = Projects.objects.all().count()
	total_num_of_outreaches = Outreaches.objects.all().count()
	total_num_of_sliders = Sliders.objects.all().count()
	total_num_of_testimonials = Testimonials.objects.all().count()
	total_num_of_users = Account.objects.all().count()
	total_num_of_donations = Donation.objects.all().count()
	context = {
		"total_num_of_blogs": total_num_of_blogs,
		"total_num_of_projects": total_num_of_projects,
		"total_num_of_outreaches": total_num_of_outreaches,
		"total_num_of_sliders": total_num_of_sliders,
		"total_num_of_testimonials": total_num_of_testimonials,
		"total_num_of_users": total_num_of_users,
		"total_num_of_donations": total_num_of_donations
	}
	return render(request, 'account/dashboard.html', context)

def logout_view(request):
	logout(request)
	return redirect('home')


def account_view(request):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')


	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
				"email": request.POST['email'],
				"username": request.POST['username'],
				"first_name": request.POST['first_name'],
				"last_name": request.POST['last_name'],
			}
			form.save()
			return redirect('account_update_success')
	else:
		form = AccountUpdateForm(
				initial = {
					"email": request.user.email,
					"username": request.user.username,
					"first_name": request.user.first_name,
					"last_name": request.user.last_name,
				}
			)

	context['account_form'] = form
	return render(request, 'account/account.html', context)


def must_authenticate_view(request):
	return render(request, 'account/must_authenticate.html', context)


def all_post_screen_view(request):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	blogs = Blogs.objects.all().order_by('-id')
	context['blogs'] = blogs
	return render(request, 'account/all_post.html', context)

def all_project_screen_view(request):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	projects = Projects.objects.all().order_by('-id')
	context['projects'] = projects
	return render(request, 'account/all_project.html', context)

def all_outreach_screen_view(request):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	outreaches = Outreaches.objects.all().order_by('-id')
	context['outreaches'] = outreaches
	return render(request, 'account/all_outreach.html', context)

def all_slider_screen_view(request):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	sliders = Sliders.objects.all().order_by('-id')
	context['sliders'] = sliders
	return render(request, 'account/all_slider.html', context)

def all_testimonials_screen_view(request):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	testimonials = Testimonials.objects.all().order_by('-id')
	context['testimonials'] = testimonials
	return render(request, 'account/all_testimony.html', context)

def all_contacts_screen_view(request):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	contacts = Contact.objects.all().order_by('-id')
	context['contacts'] = contacts
	return render(request, 'account/all_contact.html', context)

def all_users_screen_view(request):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	users = Account.objects.all().order_by('-id')
	context['users'] = users
	return render(request, 'account/all_users.html', context)

def all_trustee_screen_view(request):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	if not request.user.is_superuser:
		return redirect('my_trustee')
	trustees = Bio.objects.all().order_by('-id')
	context['trustees'] = trustees
	return render(request, 'account/all_trustee.html', context)

def my_trustee_screen_view(request):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	author = Account.objects.filter(email=user.email).first()
	trustees = Bio.objects.filter(author=author).order_by('-id')
	context['trustees'] = trustees
	return render(request, 'account/my_trustee.html', context)


def detail_users_view(request, id):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	user_post = get_object_or_404(Account, id=id)
	context['user_post'] = user_post
	return render(request, 'account/detail_user.html', context)

def users_delete_view(request, id):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	users = Account.objects.filter(id=id)
	users.delete()
	return redirect('all_users')


def detail_contact_view(request, id):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	contact_post = get_object_or_404(Contact, id=id)
	context['contact_post'] = contact_post
	return render(request, 'account/detail_contact.html', context)

def contact_delete_view(request, id):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	contact = Contact.objects.filter(id=id)
	contact.delete()
	return redirect('all_contact')


def all_subscribe_screen_view(request):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	# url_all_subscriber = request.build_absolute_uri()
	# request.session['all_subscriber_url'] = url_all_subscriber

	subscribers = Subscribe.objects.all().order_by('-id')
	context['subscribers'] = subscribers
	return render(request, 'account/all_subscribers.html', context)

def detail_subscribe_view(request, id):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	subscribe_post = get_object_or_404(Subscribe, id=id)
	context['subscribe_post'] = subscribe_post
	return render(request, 'account/detail_subscribe.html', context)

def subscribe_delete_view(request, id):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	subscribe = Subscribe.objects.filter(id=id)
	subscribe.delete()
	return redirect('all_subscribers')

def account_update_success_view(request):
	user = request.user
	if not request.user.is_authenticated:
		return redirect('login')

	return render(request, 'account/account_update_success_view.html', context)