from django.shortcuts import render
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination


# Create your views here.

@api_view(["GET","POST"])
def productCrud(request):
    if request.method == "GET":

        partial_name = request.GET.get("name")
        min_price = request.GET.get("min_price")
        max_price = request.GET.get("max_price")

        if min_price is not None:
            try:
                min_price = float(min_price)
            except ValueError:
                return Response({"detail": "Invalid min_price value"}, status=400)
        if max_price is not None:
            try:
                max_price = float(max_price)
            except ValueError:
                return Response({"detail": "Invalid max_price value"}, status=400)

        if partial_name is None:
            my_products = Product.objects.all()
            if min_price is not None and max_price is not None:
                my_products = my_products.filter(price__gte=min_price, price__lte=max_price)
            elif min_price is not None:
                my_products = my_products.filter(price__gte=min_price)
            elif max_price is not None:
                my_products = my_products.filter(price__lte=max_price)
            
            paginator = PageNumberPagination()
            paginator.page_size = 2
            paginated_queryset = paginator.paginate_queryset(my_products, request)

            if my_products.exists():
                serializer = ProductSerializer(paginated_queryset, many=True)
                return Response(serializer.data, status=200)
            else: 
                return Response({"detail": "Data not found"}, status=404)
            
        my_products = Product.objects.filter(name__icontains=partial_name)

        if my_products.exists():
            paginator = PageNumberPagination()
            paginator.page_size = 2
            paginated_queryset = paginator.paginate_queryset(my_products, request)
            serializer = ProductSerializer(my_products, many=True)
            return Response(serializer.data)
        
        return Response({"detail": "Data not found"}, status=404)
    
    if request.method=="POST":

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Creates and saves new Product instance
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(["GET","PUT","DELETE"])
def idSpecificProductCrud(request, id):

    if request.method == "GET":

        my_product = Product.objects.filter(id=id)

        if my_product.exists():
            serializer = ProductSerializer(my_product, many=True)
            return Response(serializer.data, status=200)
        else:
            return Response({"detail": "Data not found"}, status=404)
        
    if request.method == "PUT":

        my_product = Product.objects.filter(id=id).first()
        if my_product is None:
            return Response({"detail": "Data not found"}, status=404)
        
        serializer = ProductSerializer(my_product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        
        return Response(serializer.errors, status=400)
    
    if request.method == "DELETE":

        product = Product.objects.filter(id=id).first()

        if product is None:
            return Response({"detail": "Data not found"}, status=404)
        
        product_name = product.name
        product.delete()
        return Response({"detail": f"Product-{product_name} has been deleted."}, status=200)
    
    return Response({"detail": f"The following HTTP method - {request.method} is wrong"}, status=405)