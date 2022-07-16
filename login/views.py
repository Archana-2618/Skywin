from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class AddUser(generics.ListCreateAPIView):
    # get method handler
    queryset = User.objects.all()#filter(user_type="sub dealer")
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # if self.check_signin_details(self.request.data):
        self.perform_create(serializer)


        response = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'message': 'User created successfully',
            'data': serializer.data
        }
        return Response(response)




class Login(generics.GenericAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid():
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)



class Logout(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid():
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)





"""User Input"""
from .models import Input
from .serializers import InputSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Input_List(APIView):

    def get(self, request):
        data = Input.objects.all()
        serializer = InputSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
            'status': 'success',
            'code': status.HTTP_201_CREATED,
            'message': 'Details added successfully',
            'data': serializer.data
        }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Input_Detail(APIView):

    def get_object(self, pk):
        try:
            return Input.objects.get(pk=pk)
        except Input.DoesNotExist:
            raise Http404

    def get(self, pk):
        data = self.get_object(pk)
        serializer = InputSerializer(data)
        return Response(serializer.data)

    def put(self, request, pk):
        data = self.get_object(pk)
        serializer = InputSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
            'status': 'success',
            'code': status.HTTP_201_CREATED,
            'message': 'Updated successfully',
            'data': serializer.data
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        data = self.get_object(pk)
        data.delete()
        response = {
            'status': 'success',
            'code': status.HTTP_204_NO_CONTENT,
            'message': 'Deleted successfully',
            'data': serializer.data
            }
        return Response(response)



"""weight"""
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Manual_List(APIView):

    def get(self, request):
        data = Input.objects.all()
        serializer = ManualSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ManualSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
            'status': 'success',
            'code': status.HTTP_201_CREATED,
            'message': 'Details added successfully',
            'data': serializer.data
        }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Manual_Detail(APIView):

    def get_object(self, pk):
        try:
            return Input.objects.get(pk=pk)
        except Input.DoesNotExist:
            raise Http404

    def get(self, pk):
        data = self.get_object(pk)
        serializer = ManualSerializer(data)
        return Response(serializer.data)

    def put(self, request, pk):
        data = self.get_object(pk)
        serializer = ManualSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
            'status': 'success',
            'code': status.HTTP_201_CREATED,
            'message': 'Updated successfully',
            'data': serializer.data
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        data = self.get_object(pk)
        data.delete()
        response = {
            'status': 'success',
            'code': status.HTTP_204_NO_CONTENT,
            'message': 'Deleted successfully',
            'data': serializer.data
            }
        return Response(response)

class Direct_List(APIView):

    def get(self, request):
        data = Weight.objects.all()
        serializer = DirectSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DirectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
            'status': 'success',
            'code': status.HTTP_201_CREATED,
            'message': 'Details added successfully',
            'data': serializer.data
        }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Direct_Detail(APIView):

    def get_object(self, pk):
        try:
            return Weight.objects.get(pk=pk)
        except Weight.DoesNotExist:
            raise Http404

    def get(self, pk):
        data = self.get_object(pk)
        serializer = DirectSerializer(data)
        return Response(serializer.data)

    def put(self, request, pk):
        data = self.get_object(pk)
        serializer = DirectSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
            'status': 'success',
            'code': status.HTTP_201_CREATED,
            'message': 'Updated successfully',
            'data': serializer.data
        }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        data = self.get_object(pk)
        data.delete()
        response = {
            'status': 'success',
            'code': status.HTTP_204_NO_CONTENT,
            'message': 'Deleted successfully',
            'data': serializer.data
            }
        return Response(response)

class Quantity_List(APIView):

    def get(self, request):
        data = Weight.objects.all()
        serializer = QuantitySerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuantitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
            'status': 'success',
            'code': status.HTTP_201_CREATED,
            'message': 'Details added successfully',
            'data': serializer.data
        }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Quantity_Detail(APIView):

    def get_object(self, pk):
        try:
            return Weight.objects.get(pk=pk)
        except Weight.DoesNotExist:
            raise Http404

    def get(self, pk):
        data = self.get_object(pk)
        serializer = QuantitySerializer(data)
        response = {
            'status': 'success',
            'code': status.HTTP_201_CREATED,
            'message': 'fetch all data successfully',
            'data': serializer.data
        }
        return Response(response)

    def put(self, request, pk):
        data = self.get_object(pk)
        serializer = QuantitySerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
            'status': 'success',
            'code': status.HTTP_201_CREATED,
            'message': 'Updated successfully',
            'data': serializer.data
        }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        data = self.get_object(pk)
        data.delete()
        response = {
            'status': 'success',
            'code': status.HTTP_201_CREATED,
            'message': 'Deleted successfully',
            'data': serializer.data
        }
        return Response(response)

