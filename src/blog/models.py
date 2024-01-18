from django.db import models


from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver



# Create your models here.

def upload_location(instance, filename, **kwargs):
	file_path = 'blog/{author_id}/{title}-{filename}'.format(
			author_id=str(instance.author.id), title=str(instance.title), filename=filename
		)
	return file_path

class Blogs(models.Model):
	title					= models.CharField(max_length=120, null=False, blank=False)
	body					= models.TextField(max_length=5000, null=False, blank=False)
	image					= models.ImageField(upload_to=upload_location, null=False, blank=False)
	date_published			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	author 					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	slug 					= models.SlugField(blank=True, unique=True)

	def __str__(self):
		return self.title

	# class Meta:
	# 	verbose_name = "News"
	# 	verbose_name_plural = "List of all the News"

@receiver(post_delete, sender=Blogs)
def submission_delete(sender, instance, **kwargs):
	instance.image.delete(False)


def pre_save_blogs_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.author.username + "-" + instance.title)

pre_save.connect(pre_save_blogs_receiver, sender=Blogs)




class BlogComment(models.Model):
	body					= models.CharField(max_length=1000, null=False, blank=False)
	blog_post_id			= models.CharField(max_length=120, null=False, blank=False)
	date_published			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	author 					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	

	def __str__(self):
		return self.body

	# class Meta:
	# 	verbose_name = "News"
	# 	verbose_name_plural = "List of all the News"

@receiver(post_delete, sender=BlogComment)
# def submission_delete(sender, instance, **kwargs):
# 	 instance.image.delete(False)


def pre_save_blog_comment_receiver(sender, instance, *args, **kwargs):
	pre_save.connect(pre_save_blog_comment_receiver, sender=BlogComment)


class BlogCommentReply(models.Model):
	body					= models.CharField(max_length=1000, null=False, blank=False)
	post_type				= models.CharField(max_length=120, null=False, blank=False)
	comment_type			= models.CharField(max_length=120, null=False, blank=False)
	date_published			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	author 					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	

	def __str__(self):
		return self.body

	# class Meta:
	# 	verbose_name = "News"
	# 	verbose_name_plural = "List of all the News"

@receiver(post_delete, sender=BlogCommentReply)
# def submission_delete(sender, instance, **kwargs):
# 	 instance.image.delete(False)


def pre_save_blog_comment_reply_receiver(sender, instance, *args, **kwargs):
	pre_save.connect(pre_save_blog_comment_reply_receiver, sender=BlogCommentReply)

