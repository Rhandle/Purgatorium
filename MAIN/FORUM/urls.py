from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include("PURGATORIUM.urls")), 
    path('tinymce/', include('tinymce.urls')),
    path('account/', include('register.urls')),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
	]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)