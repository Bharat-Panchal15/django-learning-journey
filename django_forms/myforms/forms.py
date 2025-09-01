from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','author']
    
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
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)