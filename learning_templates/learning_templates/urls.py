from django.contrib import admin
from django.urls import path,include
from basic_app.views import index

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('basic_app/',include('basic_app.urls'))
]
