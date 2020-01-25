from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label = "", required = True, max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'name'}))
    email = forms.EmailField(label = "", required = True, max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'email'}))
    phone = forms.RegexField(label = "", regex=r'^\+?1?\d{11,13}$', widget=forms.TextInput(attrs={'placeholder': 'mobile number'}))
    message = forms.CharField(label = "", widget=forms.Textarea(attrs={'placeholder': 'Write your messages here...', 'rows': '4'}))