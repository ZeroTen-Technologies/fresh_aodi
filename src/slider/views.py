from django.shortcuts import render, redirect, get_object_or_404
from slider.models import Sliders
from slider.forms import CreateSliderForm, UpdateSliderPostForm
from account.models import Account 

# Create your views here.
context = {}


def slider_view(request):
	sliders = Sliders.objects.all().order_by('-id')
	context['sliders'] = sliders
	return render(request, 'slider/slider.html', context)


def create_slider_view(request):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')
	

	form = CreateSliderForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		return redirect('slider:success')

	context['form'] = form

	return render(request, 'slider/create_slider.html', context)

def detail_slider_view(request, slug):


	slider_post = get_object_or_404(Sliders, slug=slug)

	context['slider_post'] = slider_post
	return render(request, 'slider/detail_slider.html', context)


def edit_slider_view(request, slug):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')

	slider_post = get_object_or_404(Sliders, slug=slug)
	if request.POST:
		form = UpdateSliderPostForm(request.POST or None, request.FILES or None, instance=slider_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return redirect('slider:edit_success')
			slider_post = obj
	form = UpdateSliderPostForm(
			initial = {
					"title": slider_post.title,
					"body": slider_post.body,
					"link": slider_post.link,
					"image": slider_post.image,
					"slug": slider_post.slug
			}

		)
	context['form'] = form
	return render(request, 'slider/edit_slider.html', context)


def slider_delete_view(request, id):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')

	slider = Sliders.objects.filter(id=id)
	slider.delete()
	return redirect('all_slider')


def slider_success_view(request):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')

	return render(request, 'slider/success_view.html', context)

def slider_edit_success_view(request):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')
		
	return render(request, 'slider/edit_success_view.html', context)