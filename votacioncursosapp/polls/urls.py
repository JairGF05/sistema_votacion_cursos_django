from django.urls import path
#El punto quiere decir que vamos a importar algo del paquete actual de donde esta el archivo 
#en este caso pools seria lo mismo decir from polls
from . import views 

#definiendo la misma variable urlpatterns
urlpatterns = [
    path("", views.index, name= "index")
]
