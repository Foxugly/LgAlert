from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from alert.views import AlertCreateView
from .views import home, confirm


urlpatterns = [
    path('', home, name="home"),
    path('form/', AlertCreateView.as_view(), name='alert_add'),
    path('confirm/', confirm, name='confirm'),
    path('tinymce/', include('tinymce.urls')),
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
