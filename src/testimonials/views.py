from django.shortcuts import render, redirect, get_object_or_404
from testimonials.models import Testimonials
from testimonials.forms import CreateTestimonyForm, UpdateTestimonyPostForm
from account.models import Account 

# Create your views here.
context = {}


def testimonials_screen_view(request):
	testimonials = Testimonials.objects.all().order_by('-id')
	context['testimonials'] = testimonials
	return render(request, 'testimonials/testimonials.html', context)


def create_testimonials_view(request):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')
	

	form = CreateTestimonyForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		return redirect('testimonials:success')

	context['form'] = form

	return render(request, 'testimonials/create_testimonials.html', context)

def detail_testimonials_view(request, slug):


	testimony_post = get_object_or_404(Testimonials, slug=slug)

	context['testimony_post'] = testimony_post
	return render(request, 'testimonials/detail_testimonials.html', context)


def edit_testimonials_view(request, slug):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')

	testimony_post = get_object_or_404(Testimonials, slug=slug)
	if request.POST:
		form = UpdateTestimonyPostForm(request.POST or None, request.FILES or None, instance=testimony_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return redirect('testimonials:edit_success')
			testimony_post = obj
	form = UpdateTestimonyPostForm(
			initial = {
					"title": testimony_post.title,
					"body": testimony_post.body,
					"image": testimony_post.image,
					"slug": testimony_post.slug
			}

		)
	context['form'] = form
	return render(request, 'testimonials/edit_testimonials.html', context)


def testimonials_delete_view(request, id):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')

	testimony = Testimonials.objects.filter(id=id)
	testimony.delete()
	return redirect('all_testimony')

def testimony_success_view(request):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')

	return render(request, 'testimonials/success_view.html', context)

def testimony_edit_success_view(request):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')
		
	return render(request, 'testimonials/edit_success_view.html', context)