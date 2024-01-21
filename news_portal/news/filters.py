from django_filters import FilterSet, CharFilter, DateTimeFilter, ModelChoiceFilter
from django.forms import DateTimeInput
from .models import *

class PostFilter(FilterSet):
    title__contains = CharFilter(field_name='title', lookup_expr='icontains', label='Название содержит')
    categories__contains = ModelChoiceFilter(field_name='categories', queryset=Category.objects.all(), label='Категория')
    added_after = DateTimeFilter(
        field_name='timedate',
        lookup_expr='gte',
        label = 'Опубликовано после',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = ['title__contains', 'categories__contains', 'added_after']