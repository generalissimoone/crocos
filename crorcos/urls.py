from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zapros_klienta.urls')),
    path('chat/', include('chatbot.urls'))
]