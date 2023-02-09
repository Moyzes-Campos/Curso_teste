from django.urls import path
from .views import DocumentList

urlpatterns = [
    path('list', DocumentList.as_view(), name='document_list'),
]
