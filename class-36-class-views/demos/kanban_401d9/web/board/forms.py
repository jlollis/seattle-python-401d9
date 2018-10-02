from django.forms import ModelForm
from .models import Card, Category

class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ['name', 'description']

