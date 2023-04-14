from django.urls import path
#El punto quiere decir que vamos a importar algo del paquete actual de donde esta el archivo 
#en este caso pools seria lo mismo decir from polls
from . import views 

#variable d enombre de aplicacion
app_name = "polls"

#definiendo la misma variable urlpatterns
urlpatterns = [
    #ex: /polls/
    path("", views.index, name="index"),
    #ex: /polls/5/
    path("<int:question_id>/detail", views.detail, name="detail"),
    #ex: /polls/5/results
    path("<int:question_id>/results", views.results, name="results"),
    #ex: /polls/5/vote
    path("<int:question_id>/vote", views.vote, name="vote"),
]
