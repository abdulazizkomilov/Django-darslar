from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Blog

class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'email', 'first_name', 'last_name']



class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['author', 'like', 'participants']

