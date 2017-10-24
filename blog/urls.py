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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

# from posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # two ways to map URLs when using function based views
 #    url(r'^posts/$', views.post_home), # this is less preferred
 #    """
 #    when you have multiple apps being imported, this will cause problems. i.e.

 #    from users import views
 #    from posts import views

	# django won't know which view we are referring to in our URL
 #    """

    url(r'^posts/$', "posts.views.post_home"), # this is better because it's more specific
]
