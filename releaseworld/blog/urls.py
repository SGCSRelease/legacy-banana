from django.conf.urls import url
from blog.views import login_check, blog_home


urlpatterns = [
    url(r'^$', login_check, name='login_check'),
    url(r'^(?P<username>\w+)/$', blog_home, name='blog_home'),
]
