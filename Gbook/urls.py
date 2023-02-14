from . import views
from django.urls import path

urlpatterns = [
    path('verse/<str:book>+<int:chapter>/<int:verse>/', views.get_verse, name='verse'),
]