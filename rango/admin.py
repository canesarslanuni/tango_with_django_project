#Here I register the classes I want included in the admin interface
#The slug field is automatically populated

from django.contrib import admin
from rango.models import Category, Page
...
# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)
...
