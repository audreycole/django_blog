"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

""" 
^ for beginning of the text
$ for end of text
\d for a digit
+ to indicate that the previous item should be repeated at least once
() to capture part of the pattern
"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('my_blog.urls')), # Redirect anything from localhost:8000/ to the urls for our my_blog app
]
