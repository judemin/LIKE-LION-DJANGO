import jwt
from django.http import JsonResponse
from django.conf import settings


def jwt_required(f):
    def wrap(request, *args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return JsonResponse({"msg": "Authorization header is missing"}, status=401)

        try:
            # "Bearer " Replacement
            if "Bearer " in token:
                token = token.replace("Bearer ", "", 1)

            # Token Validation
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            request.user_id = payload["id"]  # Add UserID into request

        except jwt.ExpiredSignatureError:
            return JsonResponse({"msg": "Token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"msg": "Invalid token"}, status=401)

        return f(request, *args, **kwargs)

    return wrap
