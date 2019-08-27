from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _







urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls', namespace='app')),
    #path('', include('instructor.urls', namespace='instructor')),
    path('', include('teacher.urls', namespace='teacher')),
    path('accounts/', include('django.contrib.auth.urls')),
    
   

    


]


if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







