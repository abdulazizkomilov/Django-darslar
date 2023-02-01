//how to send emails in django?
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your-username@gmail.com'
EMAIL_HOST_PASSWORD = 'your-password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


python manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('test email', 'hello world', to=['test@email.com'])


python manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('test email', 'hello world', 'your@email.com', ['test@email.com'])




#Source: https://stackoverflow.com/questions/6914687

