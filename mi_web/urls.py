"""
URL configuration for mi_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as views_core
from portfolio import views as views_portfolio

urlpatterns = [
    #path del core
    path('', views_core.home, name='home'),
    path('about-me/', views_core.about, name='about'),
    # path('contact/', views_core.contact, name='contact'),
    
    #path de portfolio
    path('portfolio/', views_portfolio.portfolio, name='portfolio'),
    
    #path del admin
    path('admin/', admin.site.urls),
]

# para ver archivos media en fase de prueba
from django.conf import settings

if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)