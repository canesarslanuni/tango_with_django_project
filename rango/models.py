from django.db import models
from django.template.defaultfilters import slugify

#Both of these classes inherit from the "Model" base class (django.db.models.Model)

#The first class represents the categories and the second class represents the pages where there is a one to many relationship between category and page in that order
#The field "category" in model "Page" is a "ForeignKey"
#The slugify() function from Django replaces the whitespace with hyphens and saves the URL

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True) #Ensures that the slug field is unique

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name


class Page(models.Model):
	category = models.ForeignKey(Category, 'on_delete')
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.title
