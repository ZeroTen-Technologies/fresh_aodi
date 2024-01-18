from django.db import models

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver



# Create your models here.

def upload_location(instance, filename, **kwargs):
	file_path = 'bio/{author_id}/{title}-{filename}'.format(
			author_id=str(instance.author.id), title=str(instance.title), filename=filename
		)
	return file_path

class Bio(models.Model):
	title					= models.CharField(max_length=120, null=True, blank=True)
	governing_board			= models.CharField(max_length=120, null=True, blank=True)
	founding_trustees		= models.CharField(max_length=120, null=True, blank=True)
	appointed_trustees		= models.CharField(max_length=120, null=True, blank=True)
	amb_membership			= models.CharField(max_length=120, null=True, blank=True)
	project_facilitator		= models.CharField(max_length=120, null=True, blank=True)
	volunteer				= models.CharField(max_length=120, null=True, blank=True)
	associate_membership	= models.CharField(max_length=120, null=True, blank=True)
	body					= models.TextField(max_length=5000, null=True, blank=True)
	image					= models.ImageField(upload_to=upload_location, null=False, blank=True)
	date_published			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	author 					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	slug 					= models.SlugField(blank=True, unique=False)

	def __str__(self):
		return self.title

	# class Meta:
	# 	verbose_name = "News"
	# 	verbose_name_plural = "List of all the News"

@receiver(post_delete, sender=Bio)
def submission_delete(sender, instance, **kwargs):
	instance.image.delete(False)


def pre_save_bio_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.author.first_name + "-" + instance.author.last_name)

pre_save.connect(pre_save_bio_receiver, sender=Bio)
