from django.shortcuts import render, redirect

from .forms import LinkForm, CategoryForm
from .models import Link


def index(request):
    links = Link.objects.all()
    context = {
        'links': links,
    }
    return render(request, 'links/index.html', context)

def link_create(request):
    if request.method == 'POST':
        link_form = LinkForm(request.POST)
        if link_form.is_valid():
            cleaned_url = link_form.cleaned_data['url']
            if Link.objects.filter(url=cleaned_url).exists():
                existent_link = Link.objects.get(url=cleaned_url)
                existent_link.categories.add(*link_form.cleaned_data['categories'])
                existent_link.times_saved += 1                
                existent_link.save()                                
            else:
                link_form.save()
            return redirect('links:link_create')
    else:
        link_form = LinkForm()
    context = {
        'link_form': link_form,
    }
    return render(request, 'links/link_form.html', context)

def category_create(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('links:category_create')
    else:
        category_form = CategoryForm()
    context = {
        'category_form': category_form,
    }
    return render(request, 'links/category_create.html', context)
