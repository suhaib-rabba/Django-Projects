
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
from django.urls import include
from trail.views import trail_view
urlpatterns = [
    path('',trail_view)
]
