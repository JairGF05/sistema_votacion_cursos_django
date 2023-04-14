from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse
from  .models import Question

#creación de función index
def index(request):
    #Objeto de tipo Queryset con todas las preguntas
    latest_question_list = Question.objects.all()
    #Entonces ahora retornamos a nuestro template index.html
    #al estar dentro de la carpeta templates no hace falta especificar esta carpeta "templates" como tal
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })


#Creación de vistas o funciones 
def detail(request, question_id):
    '''
    Esto se realizara de una forma mas eficaz, de modo que si no e encuentra la pregunta,
    Django nos ayude con el manejo de errores, en caso de qu eno encuentre la llave, va a 
    elevar el error 404 por nosotros
    '''
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/detail.html", {
        "question": question,
    })
    

def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de  la pregunta número: {question_id} ")


def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta número: {question_id} ")