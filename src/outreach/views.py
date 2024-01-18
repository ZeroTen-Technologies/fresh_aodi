from django.shortcuts import render, redirect, get_object_or_404
from outreach.models import Outreaches
from outreach.forms import CreateOutreachForm, UpdateOutreachPostForm
from account.models import Account 

# Create your views here.
context = {}


def outreach_view(request):
	outreaches = Outreaches.objects.all().order_by('-id')
	context['outreaches'] = outreaches
	return render(request, 'outreach/outreach.html', context)


def create_outreach_view(request):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')
	

	form = CreateOutreachForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		return redirect('outreach:success')

	context['form'] = form

	return render(request, 'outreach/create_outreach.html', context)

def detail_outreach_view(request, slug):


	outreach_post = get_object_or_404(Outreaches, slug=slug)

	context['outreach_post'] = outreach_post
	return render(request, 'outreach/detail_outreach.html', context)


def edit_outreach_view(request, slug):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')

	outreach_post = get_object_or_404(Outreaches, slug=slug)
	if request.POST:
		form = UpdateOutreachPostForm(request.POST or None, request.FILES or None, instance=outreach_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return redirect('outreach:edit_success')
			outreach_post = obj
	form = UpdateOutreachPostForm(
			initial = {
					"title": outreach_post.title,
					"body": outreach_post.body,
					"image": outreach_post.image,
					"slug": outreach_post.slug
			}

		)
	context['form'] = form
	return render(request, 'outreach/edit_outreach.html', context)


def outreach_delete_view(request, id):

	if not request.user.is_authenticated:
		return redirect('login')

	outreach = Outreaches.objects.filter(id=id)
	outreach.delete()
	return redirect('all_outreach')


def outreach_success_view(request):

	if not request.user.is_authenticated:
		return redirect('login')

	return render(request, 'outreach/success_view.html', context)

def outreach_edit_success_view(request):

	if not request.user.is_authenticated:
		return redirect('login')
		
	return render(request, 'outreach/edit_success_view.html', context)