from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.paginaweb),

    path('macargafron/', views.macargafron, name="macargafron"),
    path('mavolqueta/', views.mavolqueta, name="mavolqueta"),
    path('maexcavado/', views.maexcavado, name="maexcavado"),
    path('mamotonive/', views.mamotonive, name="mamotonive"),
    path('marodillo/', views.marodillo, name="marodillo"),
]
