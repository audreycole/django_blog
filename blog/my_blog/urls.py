from django.conf.urls import url
from . import views

""" 
^ for beginning of the text
$ for end of text
\d for a digit
+ to indicate that the previous item should be repeated at least once
() to capture part of the pattern
"""

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # Match localhost:8000/ to the view "post_list"
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/create/$', views.post_create, name='post_create'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    
]