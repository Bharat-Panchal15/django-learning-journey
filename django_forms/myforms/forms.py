from django import forms
from django.core.validators import MinLengthValidator, RegexValidator
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','author','image']
    
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title.lower() == 'test':
            raise forms.ValidationError("The title 'test' is deprecated. Please choose another title.")
        return title
    
    def clean_author(self):
        author = self.cleaned_data.get('author')
        if author and author.lower() == 'admin':
            raise forms.ValidationError("The name 'Admin' is reserved. Please choose another name.")
        return author
    
    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        
        if content and len(content) < 20:
            self.add_error("content","Content must be atleast of 20 characters long.")

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, validators=[MinLengthValidator(3)])
    email = forms.EmailField()
    phone = forms.CharField(validators=[RegexValidator(r'^\d{10}$','Enter a valid 10-digit phone number')])
    message = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)