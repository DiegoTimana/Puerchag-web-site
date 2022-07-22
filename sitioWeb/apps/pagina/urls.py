from django.urls import include, path
from . import views
from apps.pagina.views import contactar

urlpatterns = [
    path('index.html', views.index),
    path('contact.html', views.contact),
    path('contactar/', contactar),
    path('teachers.html', views.teachers),
    path('single.html', views.single),
    path('single-sidebar.html', views.singleSidebar),
    path('gallery-4-column.html', views.galeria)
]