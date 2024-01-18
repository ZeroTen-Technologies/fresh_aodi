from django.db import models

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver



# Create your models here.


class Subscribe(models.Model):
	name					= models.CharField(max_length=120, null=False, blank=False)
	email					= models.EmailField(verbose_name="email", max_length=60, blank=False)
	date_published			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	slug 					= models.SlugField(blank=True, unique=False)

	def __str__(self):
		return self.name

	# class Meta:
	# 	verbose_name = "News"
	# 	verbose_name_plural = "List of all the News"

@receiver(post_delete, sender=Subscribe)
# def submission_delete(sender, instance, **kwargs):
# 	 instance.image.delete(False)


def pre_save_subscribe_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.name + "-" + "newsletter")

pre_save.connect(pre_save_subscribe_receiver, sender=Subscribe)




class Contact(models.Model):
	fname					= models.CharField(max_length=120, null=False, blank=True)
	email					= models.EmailField(verbose_name="email", max_length=60, blank=True)
	subject					= models.CharField(max_length=120, null=False, blank=True)
	message					= models.TextField(max_length=5000, null=False, blank=True)
	date_published			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	slug 					= models.SlugField(blank=True, unique=False)

	def __str__(self):
		return self.fname

	# class Meta:
	# 	verbose_name = "News"
	# 	verbose_name_plural = "List of all the News"

@receiver(post_delete, sender=Contact)
# def submission_delete(sender, instance, **kwargs):
# 	 instance.image.delete(False)


def pre_save_contact_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.fname + '-' + 'inquiry')

pre_save.connect(pre_save_contact_receiver, sender=Contact)


class Donation(models.Model):
	full_name				= models.CharField(max_length=120, null=False, blank=False)
	email					= models.EmailField(verbose_name="email", max_length=60, blank=False)
	item					= models.CharField(max_length=120, null=False, blank=False)
	item_title				= models.CharField(max_length=120, null=False, blank=False)
	item_num				= models.CharField(max_length=120, null=False, blank=False)
	amount    				= models.CharField(max_length=120, null=False, blank=False)
	currency    			= models.CharField(max_length=120, null=False, blank=False)
	body    				= models.CharField(max_length=1000, null=False, blank=False)
	date_published			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	slug 					= models.SlugField(blank=True, unique=False)

	def __str__(self):
		return self.full_name

	# class Meta:
	# 	verbose_name = "News"
	# 	verbose_name_plural = "List of all the News"

@receiver(post_delete, sender=Donation)
# def submission_delete(sender, instance, **kwargs):
# 	 instance.image.delete(False)


def pre_save_donation_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.full_name + "-" + "donation")

pre_save.connect(pre_save_donation_receiver, sender=Donation)
