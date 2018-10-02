from django.urls import path
from .views import CategoryView, CardView, CategoryCreateView

urlpatterns = [
    path('category', CategoryView.as_view(), name='category_view'),
    path('category/new', CategoryCreateView.as_view(), name='category_create_view'),
    path('card/<int:id>', CardView.as_view(), name='card_detail'),
]
