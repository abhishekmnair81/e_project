from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def searchproducts(request):
    p = None
    query = ""
    if request.method == "POST":
        query = request.POST.get('q', '').strip()  # Get and strip the query string
        if query:
            p = Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    context = {'pro': p, 'query': query}
    return render(request, 'search.html', context)
