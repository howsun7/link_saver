from django.shortcuts import render

from .forms import LinkForm, CategoryForm


def index(request):
    return render(request, 'links/index.html')

def link_create(request):
    link_form = LinkForm()
    category_form = CategoryForm()
    context = {
        'link_form': link_form,
        'category_form': category_form,
    }
    return render(request, 'links/link_form.html', context)
