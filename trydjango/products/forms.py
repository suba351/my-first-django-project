from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "Yor title"}))
    email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "class": "new-class-name two",
            "rows": 20,
            "cols": 20,
        }
        )
    )
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            return title
        else:
            raise forms.ValidationError("This is not a Valid title")

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("Wrong mail, try again!")


class RawProductForm(forms.Form):
    title = forms.CharField(label='title( label in forms )', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                            required=False,
                            widget=forms.Textarea(attrs={
                                                        "class": "new-class-name two",
                                                        "rows": 20,
                                                        "cols": 20,
                                                  }
                                )
                            )
    price = forms.DecimalField(initial=199.99)
