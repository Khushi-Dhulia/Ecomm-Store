from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def index(request):
     product = Product.objects.all()


    # category = Category.objects.all()
    # categoryID = request.GET.get('category')

     return render(request,'index.html',{'product':product} )
     # return redirect('index')

    
def men(request):
    product = Product.objects.filter(men=True)
    return render(request,'men.html',{'product':product})

def women(request):
     product = Product.objects.filter(women=True)
     return render(request, 'women.html',{'product':product})

def bag(request):
     product = Product.objects.filter(bag=True)
     return render(request, 'bag.html',{'product':product})

def watch(request):
     product = Product.objects.filter(watch=True)
     return render(request, 'watch.html',{'product':product})

def shoes(request):
     product = Product.objects.filter(shoes=True)
     return render(request, 'shoes.html',{'product':product})

def blog(request):
     return render(request,'blog.html')

def about(request):
     return render(request, 'about.html')

def contact(request):
     return render(request, 'contact.html')    
def cart(request):
     return render(request, 'cart.html')

def login(request):
        if request.method != 'POST':
                return render(request,'login.html')
        username = request.POST['username']
        psw = request.POST['psw']
        User =auth.authenticate(username=username,password=psw)
        if User is not None:
                auth.login(request,User)
                return redirect("/")
        else:
                messages.info(request,'invalid credentials')
                return redirect('login')       

def register(request):
        if request.method != 'POST':
                return render(request,'register.html')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']
        
        if psw == psw_repeat:
          if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
          elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Taken')
            return redirect('register')
          else:
            user = User.objects.create_user(username=username, password=psw,first_name=first_name,last_name=last_name,email=email)
            user.save()
            print('User Created')
           
            user =auth.authenticate(username=username,password=psw)
            if user is not None:
                auth.login(request,user)
                return redirect("/")
            else:
                messages.info(request,'invalid credentials')
                return redirect('login')  
            

        else:
          messages.info(request,'Password not matching....')  
          return redirect('register') 

def logout(request):
        auth.logout(request)    
        return redirect('/') 