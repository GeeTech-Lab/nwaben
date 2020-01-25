class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', required = True, max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'example'}))
    email = forms.EmailField(label='Your email', required = True, max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'example@email.com'}))
    phone = forms.RegexField(label='Your phone number', regex=r'^\+?1?\d{11,13}$', widget=forms.TextInput(attrs={'placeholder': '08012345678'}))
    category = forms.ChoiceField(label='', choices=SERVICES)
    description = forms.CharField(label='Service description', required = True, max_length = 300, widget=forms.TextInput(attrs={'placeholder': 'Brief description of what you need us to do for you'}))
    message = forms.CharField(label='Your message', widget=forms.Textarea)