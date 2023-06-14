from django.shortcuts import render, redirect
from django.urls import path
from  django.http import HttpResponse






# Create your views here.
def base(request):
    return render(request,"base.html")


#UserRegistration
from .forms import RegisterForm

def register_page(request):
    form=RegisterForm()
    context = {
        "title":"Registration Page",
        "form":form
    }

    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=True)
            user.set_password(user.password)
            user.save()
            return redirect('/base')
        else:
            return render(request,"register.html",context)
    return render(request,"register.html",context)

#UserLogin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def login_page(request):
    loginform=AuthenticationForm()
    if request.method=="POST":
        username=request.POST.get('username')
        pwd=request.POST.get('password')
        print(username,pwd)
        user=authenticate(username=username,password=pwd)
        print(user)
        if user!=None:
            
            login(request,user)
            print(request,user)
            return redirect("/base")
        else:
            msg='Invalid username or password'
            return render(request,'login.html',{'form':loginform,'msg':msg})
    return render(request,'login.html',{'form':loginform})

#UserLogout
from django.contrib.auth import authenticate, logout

def logout_page(request):
    print(request.user)
    logout(request)
    print(request.user)
    return redirect('/login')

#Market
from .models import Product_details,  Birds_details
def dogs_market(request):
    instances = Product_details.objects.all() 
    context = {'instances': instances}
    return render(request, 'Dogs.html', context)
def birds_market(request):
    instances = Birds_details.objects.all()  
    context = {'instances': instances}
    return render(request, 'birds.html', context)
def upcoming(request):
    return render(request,'upcoming.html')


#Orders Details
def my_order(request):
    return render(request,'orders.html')

#upload image
from PetStore.functions import handle_uploaded_file
from myapp.forms import PetImage

def upload_view(request):
    if request.method == 'POST':
        x = PetImage(request.POST, request.FILES)
        if x.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('success')  # Redirect to a success page
    else:
        x = PetImage()
        return render(request, 'upload.html',{'form':x})



# def upload_view(request):
#     if request.method == 'POST':
#         x = PetImage(request.POST, request.FILES)
#         c1=image.objects.Create(images=x)
#         c1.save()
#         return redirect('/base')
#     else:
#         x = PetImage()
#         return render(request, 'upload.html',{'form':x})



# def image_upload(request):
#     instance = Product_details.objects.first()  # Assuming you want to display the first instance
#     context = {'instance': instance}
#     return render(request, 'Dogs.html', context)

# Cookies
def set_cookie(request):
    res=render(request,"setcookie.html")
    res.set_cookie('name','ITV-Offline-Django')
    return res

def get_cookie(request):
    v=request.COOKIES.get('name','Guest')
    return render(request,'getcookie.html',{'value':v})

def del_cookie(request):
    res=render(request,'delcookie.html')
    res.delete_cookie('name')
    return res

#Sessions

def set_session(request):
    request.session['name']="Chota_Bheem"
    return render(request,"setsession.html")

def get_session(request):
    v=request.session.get('name','Guest')
    return render(request,'getsession.html',{'Value':v})

def del_session(request):
    if 'name' in request.session:
        del request.session['name']
        return render(request,'delsession.html')

#Search Bar

def search_results(request):
    query = request.GET.get('query','')
    pet = Product_details.objects.filter(title__icontains=query)
    return render(request,'search_results.html',{'query':query,'pets': pet})

#Cart
from .models import Cart
from django.http import JsonResponse

def cart_home(request):
    request.session['cart_id']=12
    request.session['user']=request.user.username
    return render(request,'Cart.html',{})

def update_cart(request):
    p = request.POST.get('price')
    q = request.POST.get('qnt')
    print(request.POST)
    cart_id = request.POST.get('cid')

    cart = Cart.objects.get(id=cart_id)
    cart.quantity = q
    cart.total_price = float(p) * int(q)
    cart.save()

    total = Cart.objects.filter(user=request.user).aggregate(total_price_sum=models.Sum('total_price'))
    total_amount = total['total_price_sum']

    Cart.amount = total_amount

    return JsonResponse({'status':True, 'totalprice':cart.total_price, 'totalamt': Cart.amount})
    