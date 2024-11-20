
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from shop.models import Categories, Product
# Create your views here.
def categories(request):
    c=Categories.objects.all()
    context={'cat':c}
    return render(request,'categories.html',context)

def products(request,i):
    c=Categories.objects.get(id=i)
    p=Product.objects.filter(category=c)
    context={'cat':c,'pro':p}
    return render(request,'products.html',context)

def details(request,i):
    p=Product.objects.get(id=i)
    context={'pro':p}
    return render(request,'details.html',context)


def register(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if p == cp:
            u = User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
            u.save()
            return redirect('shop:categories')
        else:
            return HttpResponse("Passwords should be the same")

    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']

        user = authenticate(username=u, password=p)  # checks whether the details entered by the user is correct or not

        if user:
            login(request, user)
            return redirect('shop:categories')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('shop:user_login')

from django.shortcuts import render, redirect
from .models import Categories
from django.http import HttpResponse

def add_categories(request):
    if request.method == "POST":
        n = request.POST['n']
        d = request.POST['d']
        i = request.FILES['i']

        new_category = Categories.objects.create(name=n, desc=d, image=i)
        new_category.save()

        return redirect('shop:categories')

    else:
        return render(request, 'addcategories.html')



def add_products(request):
    if request.method == "POST":
        n = request.POST['n']
        i = request.FILES.get('i')
        d = request.POST.get('d')
        p = request.POST.get('p')
        s = request.POST.get('s')
        c =request.POST.get('c')
        cat= Categories.objects.get(name=c)

        new_product = Product.objects.create(name=n, desc=d, image=i, price=p, stock=s, category=cat)
        new_product.save()

        return redirect('shop:categories')

    return render(request,'addproducts.html')

def addstock(request,i):
    p=Product.objects.get(id=i)
    if (request.method == "POST"):
        p.stock = request.POST['s']
        p.save()
        return redirect('shop:details', i)
    context={'pro':p}
    return render(request,'addstock.html',context)

