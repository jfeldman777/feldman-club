"""feldman2017 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from machina.app import board
from club import views as core_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = []

if settings.DEBUG:#в этом режиме медиафайлы берутся из статической папки MEDIA
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url('^admin/', admin.site.urls),
    url('^signup/$', core_views.signup, name='signup'),
    url('^password_change/done/$', core_views.password_change_done,
        name='password_change_done'),
    url('^reset/done/$', core_views.password_reset_done, name='password_reset_done'),
    url('^', include('django.contrib.auth.urls')),

    url('^weblog/', include('zinnia.urls')),
    url('^comments/', include('django_comments.urls')),
    url('^forum/', include(board.urls)),

    url('^quiz/', include('quiz.urls')),

    url('^', include('club.urls')),
]
