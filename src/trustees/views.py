from django.shortcuts import render, redirect, get_object_or_404, reverse
from trustees.forms import CreateTrusteeForm, UpdateTrusteePostForm
from account.models import Account 
from trustees.models import Bio

# Create your views here.

# create_trustee_view,
# 	trustee_success_view,
# 	trustee_edit_success_view,
# 	detail_trustee_view,
# 	trustee_comment_exist_view,
# 	edit_trustee_view,
# 	trustee_delete_view,
context = {}
def create_trustee_view(request):
	user = request.user
	if not user.is_authenticated:
		return redirect('login')
	

	form = CreateTrusteeForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		# if Bio.objects.filter(author=author).exists():
		# 	return redirect('home')
		obj.save()
		return redirect('trustees:success')

	context = {
		"form": form,
	}
	return render(request, 'trustees/create.html', context)

def trustee_success_view(request):
	return render(request, 'trustees/success_view.html', context)

def trustee_edit_success_view(request):
	return render(request, 'trustees/edit_success_view.html', context)

def detail_trustee_view(request):
	return render(request, 'trustees/detail_trustee.html', context)

def trustee_comment_exist_view(request):
	return render(request, 'trustees/trustee_comment_exist.html', context)

def edit_trustee_view(request, id):
	user = request.user
	if not user.is_authenticated:
		return redirect('login')

	blog_post = get_object_or_404(Bio, id=id)
	if request.POST:
		form = UpdateTrusteePostForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return redirect('trustees:edit_success')
			blog_post = obj
	form = UpdateTrusteePostForm(
			initial = {
					"title": blog_post.title,
					"body": blog_post.body,
					"image": blog_post.image,
					"slug": blog_post.slug
			}

		)
	context['form'] = form
	return render(request, 'trustees/edit_trustee.html', context)

def trustee_delete_view(request, id):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')

	trustee = Bio.objects.filter(id=id)
	trustee.delete()
	return redirect('all_trustee')