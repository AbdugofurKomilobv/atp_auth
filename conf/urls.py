
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',include('configapp.urls')),
    path('user_auth/',include('user_auth.urls'))
]
