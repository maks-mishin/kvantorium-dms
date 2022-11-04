from django.urls import path

from . import views
from .views import list_documents

urlpatterns = [
    path('', list_documents, name='my_view'),
    path(
        'delete/<int:document_id>/',
        views.document_delete,
        name='document_delete'
    ),
]
