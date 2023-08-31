from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from twilio.rest import Client


def send_sms(phone_number, activation_code):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Your activation code is: {activation_code}',
        from_='+1234567890',  # Twilio raqamingiz
        to=phone_number
    )


def check_activation_code(phone_number, activation_code):
    # Aktivatsiya kodni tekshirish va muvaffaqiyatli bo'lsa True qaytariladi, aks holda False
    # Misol uchun, aktivatsiya kodni server tomonida saqlangan ma'lumotlar bazasidan olib tekshirish mumkin
    return True  # Aktivatsiya kodni tekshirish muvaffaqiyatli


def register(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')

        # Telefon raqamni tekshirish va ro'yxatdan o'tkazish
        user = User.objects.create_user(
            username=phone_number, password='password')

        # Aktivatsiya kodi yaratish va SMS orqali yuborish
        activation_code = generate_activation_code()
        send_sms(phone_number, activation_code)

        return JsonResponse({'message': 'Ro\'yxatdan o\'tish muvaffaqiyatli amalga oshirildi'})


def activate(request):
    if request.method == 'POST':
        activation_code = request.POST.get('activation_code')
        phone_number = request.POST.get('phone_number')

        # Aktivatsiya kodni tekshirish
        if check_activation_code(phone_number, activation_code):
            # Aktivatsiya muvaffaqiyatli amalga oshirildi
            return JsonResponse({'message': 'Aktivatsiya muvaffaqiyatli amalga oshirildi'})
        else:
            # Aktivatsiyada xatolik yuz berdi
            return JsonResponse({'error': 'Aktivatsiyada xatolik yuz berdi'}, status=400)


def login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        # Kirishni tekshirish
        user = authenticate(request, username=phone_number, password=password)
        if user is not None:
            # Kirish muvaffaqiyatli amalga oshirildi
            login(request, user)
            return JsonResponse({'message': 'Kirish muvaffaqiyatli amalga oshirildi'})
        else:
            # Kirishda xatolik yuz berdi
            return JsonResponse({'error': 'Kirishda xatolik yuz berdi'}, status=400)
