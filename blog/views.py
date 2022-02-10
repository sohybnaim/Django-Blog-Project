from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Member,Post,ForbiddenWord,Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer


def home(request):  
    return render(request,'blog/home.html')


#rest Framework views here.
@api_view(['GET'])
def api_all_users(request):
    all_users = Member.objects.all()
    user_ser = UserSerializer(all_users, many=True)
    return Response(user_ser.data)
@api_view(['GET'])
def api_one_user(request, user_id):
    user = Member.objects.get(id=user_id)
    user_ser = UserSerializer(user, many=False)
    return Response(user_ser.data)
@api_view(['POST'])
def api_add_user(request):
    user_ser = UserSerializer(data=request.data)
    if user_ser.is_valid():
        user_ser.save()
        return redirect('api-all')
@api_view(['POST'])
def api_edit_user(request, user_id):
    user= Member.objects.get(id=user_id)
    user_ser = UserSerializer(data=request.data, instance=user)
    if user_ser.is_valid():
        user_ser.save()
        return redirect('api-all')
@api_view(['DELETE'])
def api_del_user(request, user_id):
    user= Member.objects.get(id=user_id)
    user.delete()
    return Response('User Deleted successfully!')