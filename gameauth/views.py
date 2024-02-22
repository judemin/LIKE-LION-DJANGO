from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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
