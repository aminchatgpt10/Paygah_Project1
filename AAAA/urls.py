
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("tour/", include("tour.urls"))
    # path('testapp/', include('testapp.urls'))
]
