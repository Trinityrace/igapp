from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^sign-up$', views.signup)
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
