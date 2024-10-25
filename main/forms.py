from django import forms
from django.core.exceptions import ValidationError

class ProjectForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', required=True)
    email = forms.EmailField(label='Your Email', required=False)  # Make it not required initially
    phone = forms.CharField(max_length=15, label='Your Phone Number', required=False)  # Make it not required initially
    contribution_type = forms.ChoiceField(
        choices=[
            ('bug_fix', 'Bug Fix'),
            ('feature', 'New Feature'),
            ('documentation', 'Documentation'),
            ('other', 'Other'),
        ],
        label='Type of Contribution',
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea,
        label='Message or Description',
        required=True
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')

        # Check if both email and phone are empty
        if not email and not phone:
            raise ValidationError('You must provide either an email address or a phone number.')

        return cleaned_data
