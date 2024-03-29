import django_filters
from django_filters import CharFilter

from django import forms

from .models import *

class RecipesFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr="icontains", label="Title")
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
        )
    class Meta:
        model = Recipe
        fields = ['title', 'category']