from django.urls import path
from basic_app.views import relative,other

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
path('relative/',relative,name='relative'),
path('other/',other,name='other'),
]
