
from django.urls import path
import blog.views



urlpatterns = [
    path('', blog.views.allbolgs,name='allblogs'),
    path('<int:blog_id>/',blog.views.detail,name='detail')

]
