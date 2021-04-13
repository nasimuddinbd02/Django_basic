from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Brand, Category,Product
from .serializers import BrandSerializer,CategorySerializer,ProductSerializer
from rest_framework import generics
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