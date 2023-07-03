from django.urls import path
from . import views

app_name = 'calculator'

urlpatterns = [
    # Post views
    path('<recipe>', views.calc, name='calc'),

]
