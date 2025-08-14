from django.urls import path
from django.conf.urls.static import static
from contact import views
from django.conf import settings
app_name = 'contact'

urlpatterns = [
    path('',views.index, name = 'index')
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_URL) #configurando o acesso das fotos via url
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT ) #configurando o acesso de artes via url