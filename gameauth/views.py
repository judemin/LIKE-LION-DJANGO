from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Modules needed to Create Logic
from django.contrib.auth.hashers import check_password
import jwt
from datetime import datetime, timedelta
from django.conf import settings

from .models import *
from .serializers import *


# Create your views here.
def index(request):
    return render(request, "index.html")


@csrf_exempt
@api_view(["POST"])
def signup(request):
    try:
        # Parse JSON from request
        data = JSONParser().parse(request)

        # Deconstructure Data
        name = data["name"]
        email = data["email"]
        password = data["password"]
        bestScore = 0

        # Check if email already exists
        if Users.objects.filter(email=email).exists():
            return JsonResponse({"msg": "Email already exists"}, status=400)

        # Hash the password
        hashed_password = make_password(password)

        # Create Model, Save model
        user = Users(
            name=name, email=email, password=hashed_password, bestScore=bestScore
        )
        user.save()

        return JsonResponse({"msg": "Success"}, status=201)
    except:
        return JsonResponse({"msg": "Failed"}, status=400)

@csrf_exempt
@api_view(["POST"])
def login(request):
    try:
        data = JSONParser().parse(request)
        email = data.get('email')
        password = data.get('password')

        # User Auth
        user = Users.objects.filter(email=email).first()

        if user and check_password(password, user.password):
            # Create JWT Token
            payload = {
                'id': str(user.id),  # MongoDB UID Str Transfer
                'exp': datetime.utcnow() + timedelta(days=1),  # Expired Date
                'iat': datetime.utcnow()  # Token Creation Time
            }
            # Get settings.SECRET_KEY
            accessToken = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            return JsonResponse({'token': accessToken}, status=200)
        else:
            return JsonResponse({'msg': 'Invalid credentials'}, status=400)
    except Exception as e:
        return JsonResponse({"msg": "Failed"}, status=400)