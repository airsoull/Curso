from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

class Category(models.Model):
	name = models.CharField(_('Name'), max_length=50)
	slug = models.SlugField(_('Slug'), max_length=255, blank=True)

	def save(self):
		self.slug = slugify(self.name)
		return super(Category, self).save()

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('products.views.product_list_by_category', kwargs={'slug': self.slug})


class Product(models.Model):
	name = models.CharField(_('Name'), max_length=50)
	category = models.ForeignKey(Category)
	description = models.TextField(_('Description'))

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('products.views.product_detail', kwargs={'pk': self.pk, 'slug': slugify(self.name)})


class Image(models.Model):
	product = models.ForeignKey(Product, related_name='images')
	image = models.ImageField(_('Image'), max_length=255, upload_to='upload/products/%Y/%m/%d/', width_field='width', height_field='height')
	width = models.PositiveIntegerField(default=0, blank=True)
	height = models.PositiveIntegerField(default=0, blank=True)
