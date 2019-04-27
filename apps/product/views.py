from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm
from product.models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(active=True)
    page = request.GET.get('page')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request,'pages/product-list.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, active=True)
    return render(request, 'pages/product-detail.html', {'product': product})


def product_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.annotate(
                search = SearchVector('name', 'oe', 'car'),
            ).filter(search=query)
    return render(request, 'pages/search.html', {'form': form, 'query': query, 'results': results})
