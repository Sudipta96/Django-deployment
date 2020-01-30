from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('Name should be start with Z')

#  name = forms.CharField(validators=[check_for_z])
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        clean_data = super().clean()
        email = clean_data.get('email')
        vmail = clean_data.get('verify_email')

        if email != vmail:
            raise forms.ValidationError("Make sure email match!")
