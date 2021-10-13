from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User



class SignUpForm(UserCreationForm):
    CATEGORY_CHOICES= [
        ('admin', 'Admin'),
        ('donor', 'Donor'),
        ('charity', 'Charity'),
        ]
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'category','password1', 'password2']:
            self.fields[fieldname].help_text = None

    email = forms.EmailField(max_length=254, required=True)
    category= forms.CharField(label='Choose Category', widget=forms.Select(choices=CATEGORY_CHOICES))
    class Meta:
        model = User
        fields = ('email' ,'username','category','password1', 'password2', )

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ('first_name','last_name','phone_number','email')