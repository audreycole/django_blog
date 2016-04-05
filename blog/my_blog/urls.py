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
]