
from django.contrib import admin
from django.urls import path, include,re_path
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('demo.urls')),
    path('search',include('search.urls')),
    # re_path(r'^silk', include('silk.urls', namespace='silk')),
    path('__debug__/', include('debug_toolbar.urls')),
]
# urlpatterns += urlpatterns('', url(r'^silk', include('silk.urls', namespace='silk')))
# urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]