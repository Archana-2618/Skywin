from django.db.models import Q
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.core.exceptions import ValidationError
from uuid import uuid4
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    user_type =serializers.CharField(
        required=True,

        )
    username = serializers.CharField(
        required=True,

        )
    password = serializers.CharField(min_length=8)
    confirm_password = serializers.CharField()

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                                              "confirm it.")
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data

    class Meta:
        model = User
        fields = ['username','user_type','mobile','password','confirm_password']




class UserLoginSerializer(serializers.ModelSerializer):
    # to accept either username or email
    mobile = serializers.IntegerField()
    password = serializers.CharField()
    token = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        # user,email,password validator
        mobile = data.get("mobile", None)
        password = data.get("password", None)
        if not mobile and not password:
            raise ValidationError("Details not entered.")
        user = None
        # if the email has been passed
        if mobile:
            user = User.objects.filter(
                Q(mobile=mobile) &
                Q(password=password)
                ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(mobile=mobile)
        else:
            user = User.objects.filter(
                Q(mobile=mobile) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(mobile=mobile)
        if user.ifLogged:
            raise ValidationError("User already logged in.")
        user.ifLogged = True
        data['token'] = uuid4()
        user.token = data['token']
        user.save()
        return data

    class Meta:
        model = User
        fields = (
            'mobile',
            'password',
            'token',
        )

        read_only_fields = (
            'token',
        )

class UserLogoutSerializer(serializers.ModelSerializer):
    token = serializers.CharField()
    status = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        token = data.get("token", None)
        print(token)
        user = None
        try:
            user = User.objects.get(token=token)
            if not user.ifLogged:
                raise ValidationError("User is not logged in.")
        except Exception as e:
            raise ValidationError(str(e))
        user.ifLogged = False
        user.token = ""
        user.save()
        data['status'] = "User is logged out."
        return data

    class Meta:
        model = User
        fields = (
            'token',
            'status',
        )




"""User Input"""

from rest_framework.serializers import ModelSerializer
from .models import Input


class InputSerializer(ModelSerializer):
    class Meta:
        model = Input
        fields = "__all__"


"""weight"""

from rest_framework import serializers
from .models import *


class ManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual_Weight
        fields = ['sub_dealer_name', 'weight_type', 'gross_weight', 'gunny_bag_weight', 'rate', 'total_amount', 'date']


class DirectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direct_Weight
        fields = ['sub_dealer_name', 'weight_type', 'net_weight', 'rate', 'total_amount', 'date']



'''Quantity'''
from rest_framework import serializers
from .models import Quantity


class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = ['quantity', 'rate', 'total_amount', 'date']
