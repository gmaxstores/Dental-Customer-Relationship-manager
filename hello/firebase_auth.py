from django.http import JsonResponse
from firebase_admin import auth
from httpx import request
from httpx import request


class FirebaseAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.headers.get('Authorization')
        if token:
            try:
                decoded_token = auth.verify_id_token(token.replace('Bearer ', ''))
                request.firebase_user = decoded_token
            except Exception:
                return JsonResponse({'error': 'Invalid Firebase token'}, status=401)
        return self.get_response(request)