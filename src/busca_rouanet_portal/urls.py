"""salicPortal URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from busca_rouanet import views as rouanet_views
from busca_rouanet import forms as rouanet_forms

from django.conf.urls import (
handler400, handler403, handler404, handler500
)



handler404 = 'rouanet_views.handler404'


urlpatterns = [
	url(r'^$', rouanet_views.projetosSearch, name='projetosSearch'),
    url(r'^projetos/$', rouanet_views.projetosSearch, name='projetosSearch'),
    url(r'^projetos/(?P<PRONAC>\d+)/$', rouanet_views.projetosDetail, name='projetosDetail'),
    url(r'^admin/', admin.site.urls),
    url(r'^contato/$', rouanet_views.contactView, name='contato'),
    url(r'^proponentes/$', rouanet_views.proponenteView, name='proponentes'),
    url(r'^proponentes/(?P<cgccpf>\d+)/$', rouanet_views.proponenteDetail, name='proponenteDetail'),
    url(r'^incentivadores/$', rouanet_views.incentivadorView, name='incentivadores'),
    url(r'^incentivadores/(?P<cgccpf>\d+)/$', rouanet_views.incentivadorDetail, name='incentivadorDetail'),
    url(r'^estatisticas/$', rouanet_views.estatisticasView, name='estatisticas'),
    url(r'^api/$', rouanet_views.apiView, name='api'),
    url(r'^sobre/$', rouanet_views.sobreView, name='sobre'),

    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html', 'authentication_form': rouanet_forms.LoginForm}),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/accounts/login'}),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
