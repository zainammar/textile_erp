from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import Profile

User = get_user_model()


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False), required=False,
        help_text="Edit mein khali chhoro to password nahi badlega.")
    phone = forms.CharField(max_length=20, required=False)
    role = forms.ChoiceField(choices=Profile.ROLES, initial=Profile.SALES)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "is_active"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            p, _ = Profile.objects.get_or_create(user=self.instance)
            self.fields["phone"].initial = p.phone
            self.fields["role"].initial = p.role
        else:
            self.fields["password"].required = True

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        if pwd:
            validate_password(pwd, self.instance)
        return pwd

    def save(self, commit=True):
        user = super().save(commit=False)
        pwd = self.cleaned_data.get("password")
        if pwd:
            user.set_password(pwd)
        user.save()
        p, _ = Profile.objects.get_or_create(user=user)
        p.phone = self.cleaned_data["phone"]
        p.role = self.cleaned_data["role"]
        p.save()
        return user
