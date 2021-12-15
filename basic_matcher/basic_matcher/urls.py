from django.contrib import admin
from django.urls import path, include

from .views import index
from CandidateFinder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('search/', include('CandidateFinder.urls'))
]
