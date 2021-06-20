from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import serializers
from .models import Product
#from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProductSerializer

# Create your views here.



@api_view(['GET'])
def HomeView(request):
    post = Product.objects.all()
    data = {"results": list(post.values("author", "author_id", "body", "category", "comments", "header_image", "id", "likes", "post_date", "snippet", "title", "title_tag"))}
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ProductList(request, *args, **kwargs):
    post = Product.objects.all()
    serializer = ProductSerializer(post, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ProductDetail(request, pk):
    post = Product.objects.get(id=pk)
    serializer = ProductSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def ProductCreate(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def ProductUpdate(request, pk):
    post = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def ProductDelete(request, pk):
    post = Product.objects.get(id=pk)
    post.delete()

    return Response('Product Succesfully Deleted!')



