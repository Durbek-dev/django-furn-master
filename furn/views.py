from django.shortcuts import render, redirect
from furn.models import *
from furn.form import Followers

def home(request):

    category = request.GET.get('category')
    if category == None:
        arrivals = Arrival.objects.all()
    else:
        arrivals = Arrival.objects.filter(category__category_name=category)

    base = Carousel.objects.all()
    blog = Blog.objects.all()
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'pages/home.html', {
        "base": base,
         "blog":blog,
         "arrivals":arrivals,
         "products":products,
         "categories":categories,
        })
def arrivals_detail(request, pk):
    arrivals_detalis = Arrival.objects.get(id=pk)
    context = {"arrivals_detalis": arrivals_detalis}
    return render(request, 'details/arrival_detail.html', context)