import os

from django.shortcuts import redirect, render, get_object_or_404
from .models import Document
from .forms import DocumentForm


def list_documents(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_document = Document(file=request.FILES['file'])
            uploaded_document.save()
            return redirect('list_documents')
        else:
            message = 'Ошибка'
    else:
        form = DocumentForm()
    all_documents = Document.objects.all()
    context = {'documents': all_documents, 'form': form}
    return render(request, 'list_documents.html', context)


def document_delete(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    document.delete()
    os.remove(document.file.path)
    return redirect('list_documents')


def document_edit(request, document_id):
    pass


def document_create(request, document_id):
    pass
