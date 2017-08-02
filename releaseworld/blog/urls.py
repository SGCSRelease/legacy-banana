from django.conf.urls import url
from blog.views import LoginCheck, BlogHome


urlpatterns = [
    url(r'^$', LoginCheck, name='login_check'),
    url(r'^<username>/$', BlogHome, name='blog_home'), 
]
