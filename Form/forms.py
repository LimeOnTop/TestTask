from django.forms import Form, Textarea, CharField, TextInput


class MessageForm(Form):
    name = CharField(
        widget=TextInput(
            attrs={'name': 'name', 'class': 'uk-input', 'placeholder': 'Write down who you want to make friends with'}))
    message = CharField(
        widget=Textarea(attrs={'name': 'message', 'class': 'uk-input', 'placeholder': 'Write your message here '}))
