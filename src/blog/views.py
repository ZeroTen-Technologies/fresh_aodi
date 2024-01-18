from django.shortcuts import render, redirect, get_object_or_404, reverse
from blog.models import Blogs, BlogComment, BlogCommentReply
from blog.forms import CreateBlogForm, UpdateBlogPostForm
from account.models import Account 

# Create your views here.

# fetch the latest five blog post
blogs = Blogs.objects.all().order_by('-id')[:3]
blog_images = Blogs.objects.all().order_by('-id')
context = {
	"blogs": blogs,
	"blog_images": blog_images,
}


def blog_screen_view(request):
	blogs = Blogs.objects.all().order_by('-id')
	context['blogs'] = blogs
	return render(request, 'blog/blog.html', context)


def create_blog_view(request):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')
	

	form = CreateBlogForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		return redirect('blog:success')

	context = {
		"form": form,
		"blog_images": blog_images,
	}

	return render(request, 'blog/create_blog.html', context)

def detail_blog_view(request, slug):

	blog_post = get_object_or_404(Blogs, slug=slug)
	comments = BlogComment.objects.filter(blog_post_id=blog_post.id).order_by('-id')
	
	context = {
		"blog_post": blog_post,
		"comments": comments,
		"blogs": blogs,
	}
	return render(request, 'blog/detail_blog.html', context)


def edit_blog_view(request, slug):

	user = request.user
	if not user.is_authenticated:
		return redirect('login')

	blog_post = get_object_or_404(Blogs, slug=slug)
	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return redirect('blog:edit_success')
			blog_post = obj
	form = UpdateBlogPostForm(
			initial = {
					"title": blog_post.title,
					"body": blog_post.body,
					"image": blog_post.image,
					"slug": blog_post.slug
			}

		)
	context['form'] = form
	return render(request, 'blog/edit_blog.html', context)


def blog_delete_view(request, id):

	if not request.user.is_authenticated:
		return redirect('login')

	blog = Blogs.objects.filter(id=id)
	blog.delete()
	return redirect('all_post')

def blog_success_view(request):

	if not request.user.is_authenticated:
		return redirect('login')

	return render(request, 'blog/success_view.html', context)

def blog_edit_success_view(request):

	if not request.user.is_authenticated:
		return redirect('login')
		
	return render(request, 'blog/edit_success_view.html', context)

def blog_comment_view(request):
	# get the comment body
	body = request.POST.get('body')
	# get the blog post id
	blog_post_id = request.POST.get('blog_post_id')
	# get the user that made the comment
	user = request.user
	author = Account.objects.filter(email=user.email).first()

	# fetch the blog post
	blog_post = get_object_or_404(Blogs, id=blog_post_id)

	# check if the comment already exist to prevent form resubmission
	if BlogComment.objects.filter(body=body, blog_post_id=blog_post_id, author=author).exists():
		return redirect('blog:blog_comment_exist')
	else:
		# Save the comment if it doesnt exist
		blog_comment = BlogComment(body=body, blog_post_id=blog_post_id, author=author)
		blog_comment.save()
		# fetch the comment by its id
		blog_comment_id = get_object_or_404(BlogComment, id=blog_comment.id)

	

	# fetch the comments that belongs to a particular blog post
	comments = BlogComment.objects.filter(blog_post_id=blog_post_id).order_by('-id')

	# create the context for the blog post and the comment
	context = {
		"blog_post": blog_post,
		"comments": comments,
		"blogs": blogs,
	}


	return render(request, 'blog/detail_blog.html', context)

def blog_comment_exist_view(request):
	return render(request, 'blog/blog_comment_exist.html', context)

def blog_comment_reply_view(request):
	# body = request.POST.get('body')
	# blog_id = request.POST.get('post_type')
	# comment_id = request.POST.get('comment_type')
	# user = request.user
	
	# author = Account.objects.filter(email=user.email).first()
	# if BlogCommentReply.objects.filter(body=body, post_type=blog_id, comment_type=comment_id, author=author).exists():
	# 	return redirect('blog')
	# else:
	# 	blog_comment_reply = BlogCommentReply(body=body, post_type=blog_id, comment_type=comment_id, author=author)
	# 	blog_comment_reply.save()
	# 	# blog_comment_reply_id = get_object_or_404(BlogCommentReply, id=blog_comment_reply.id)
	
	# blog_post = get_object_or_404(Blogs, id=blog_id)

	# comment_replys = BlogCommentReply.objects.filter(comment_type=comment_id).order_by('-id')
	# context['blog_post'] = blog_post
	# context['comment_replys'] = comment_replys
	return render(request, 'blog/detail_blog.html', context)