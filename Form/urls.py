from django.urls import path
import Form.views as view

urlpatterns = [
    path('message/', view.message, name='message'),
    path('result/', view.result, name='result'),
    path('message/standard/', view.standard, name='standard'),
]
