from django.shortcuts import render, redirect, get_object_or_404
from project.models import Projects, ProjectCategory
from project.forms import CreateProjectForm, UpdateProjectPostForm, CreateProjectCategoryForm
from account.models import Account
from project.models import ProjectCategory

# Create your views here.
context = {}
def projects_view(request):
	projects = Projects.objects.all().order_by('-id')
	context['projects'] = projects
	return render(request, 'project/projects.html', context)


def create_project_view(request):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')
	
	categorys = ProjectCategory.objects.all()

	form = CreateProjectForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		return redirect('project:success')

	context['form'] = form
	context['categorys'] = categorys
	return render(request, 'project/create_project.html', context)

def detail_project_view(request, slug):


	project_post = get_object_or_404(Projects, slug=slug)

	context['project_post'] = project_post
	return render(request, 'project/detail_project.html', context)


def edit_project_view(request, slug):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')

	categorys = ProjectCategory.objects.all()
	project_post = get_object_or_404(Projects, slug=slug)
	if request.POST:
		form = UpdateProjectPostForm(request.POST or None, request.FILES or None, instance=project_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return redirect('project:edit_success')
			project_post = obj
	form = UpdateProjectPostForm(
			initial = {
					"title": project_post.title,
					"body": project_post.body,
					"currency": project_post.currency,
					"amount": project_post.amount,
					"category": project_post.category,
					"image": project_post.image,
					"slug": project_post.slug
			}

		)
	context['form'] = form
	context['categorys'] = categorys
	return render(request, 'project/edit_project.html', context)


def project_delete_view(request, id):

	if not request.user.is_authenticated:
		return redirect('login')

	project = Projects.objects.filter(id=id)
	project.delete()
	return redirect('all_project')

def projects_category_view(request):
	projectcats = ProjectCategory.objects.all().order_by('-id')
	context['projectcats'] = projectcats
	return render(request, 'project/project_category.html', context)

def create_project_category_view(request):
	user = request.user
	if not user.is_authenticated:
		return redirect('login')
	

	form = CreateProjectCategoryForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		return redirect('project:success')

	context['form'] = form
	return render(request, 'project/create_project_category.html', context)

def all_project_in_cat(request, slug):
	projectcat_post = get_object_or_404(ProjectCategory, slug=slug)
	categorys = Projects.objects.filter(category=projectcat_post.id)
	context['projectcat_post'] = projectcat_post
	context['categorys'] = categorys
	return render(request, 'project/detailcat.html', context)

def project_success_view(request):

	if not request.user.is_authenticated:
		return redirect('login')

	return render(request, 'project/success_view.html', context)

def project_edit_success_view(request):

	if not request.user.is_authenticated:
		return redirect('login')
		
	return render(request, 'project/edit_success_view.html', context)