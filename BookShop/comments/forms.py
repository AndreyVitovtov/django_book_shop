from django.forms import ModelForm

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['book']
        labels = {
            'name': 'Enter your name: ',
            'surname': 'Enter your surname: ',
            'text': 'Enter text comment: ',
            'rating': 'Rating: ',
            'is_member': 'Is member: ',
        }
        error_messages = {
            'name': {
                'required': 'Required field',
                'max_length': 'Max length 50 symbols'
            },
            'surname': {
                'required': 'Required field',
                'max_length': 'Max length 50 symbols'
            },
            'text': {
                'required': 'Required field',
                'max_length': 'Max length 500 symbols'
            }
        }
