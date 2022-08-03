from django.urls import include, path
from . import views

urlpatterns = [
    path('index.html', views.index),
    path('contact.html', views.contact),
    path('contactar/', views.contactar),
    path('teachers.html', views.teachers),
    path('single.html', views.single),
    path('single-sidebar.html', views.singleSidebar),
    path('gallery-4-column.html', views.galeria),
    path('event-list.html', views.eventos),
    path('about-us.html', views.acerca)
]