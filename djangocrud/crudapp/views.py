from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Brand, Category,Product
from .serializers import BrandSerializer,CategorySerializer,ProductSerializer
from rest_framework import generics
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProductForm

def index(request):

    if request.method=='POST':
        try:
            form=ProductForm(request.POST)
            if form.is_valid():
               form.save(commit=True)
               return HttpResponseRedirect('/crud/product')

        except Exception as e:
           print(e) 
           return HttpResponseRedirect('/crud/product')

    else:
        prodForm=ProductForm()    
        return render(request, 'index.html', {'form':prodForm})

def signin(request):

    if request.method=='POST':
        try:
            username=request.POST['username'] 
            password=request.POST['password']

            user =authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

            return HttpResponseRedirect('/crud')

        except Exception as e:
           print(e) 
           return HttpResponseRedirect('/crud')

    else:
      
        return render(request, 'signin.html')

def signup(request):

    if request.method=='POST':
        try:
            userfrom =UserCreationForm(request.POST)
            
            if userfrom.is_valid():
                userfrom.save()
                username=userfrom.cleaned_data.get('username')
                password=userfrom.cleaned_data.get('password1')
                user=authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('index')
                return HttpResponseRedirect('signup')
        
        except Exception as e:
           print(e) 
           return HttpResponseRedirect('/crud')

    else:
        userfrom=UserCreationForm()    
        return render(request, 'signup.html',{'form':userfrom})

   

class BrandList(generics.ListCreateAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer

    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)

class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer

    

class CategoryList(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)
  
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ProductList(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)     


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer