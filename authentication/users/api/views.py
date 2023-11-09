from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from users.forms import SignUpForm


@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
        'avatar': request.user.get_avatar()
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignUpForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2')
    })

    if form.is_valid():
        user = form.save()
        user.save()

    else:
        message = form.errors.as_json()

    return JsonResponse({'message': message}, safe=False)
