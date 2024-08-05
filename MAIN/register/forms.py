from django import forms
from PURGATORIUM.models import Author


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["fullname", "bio", "profile_picture"]
        labels = {
            "fullname": "Full Name",
            "bio": "Biography",
            "profile_picture": "Profile Picture",
        }
        widgets = {
            "fullname": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "bio": forms.Textarea(attrs={"class": "form-control"}),
        }