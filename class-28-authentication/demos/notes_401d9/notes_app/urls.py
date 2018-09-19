from .views import notes_list_view, notes_detail_view
from django.urls import path


urlpatterns = [
    path('', notes_list_view, name='notes_list'),
    path('<int:pk>', notes_detail_view, name='notes_detail'),
]