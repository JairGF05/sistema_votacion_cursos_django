from django.db import models
from django.utils import timezone
import datetime

"""
En Python los nombres de clases se definen con la primer letra mayúscula
y en singular, a diferencia de en bases de datos que los nombres de las 
tablas se dfefinen en minúscula y plural
"""
#Primer modelo Question
class Question(models.Model):
    #el id es generado automaticamente por Django
    question_text = models.CharField(max_length=200) #cuando tiene Field al final es un tipo de dato que se puede usar
    pub_date = models.DateTimeField("date_published")

    #definiendo método dentro de la clase para mostrar información
    #todo método d euna clase como primer atributo lleva siempre self
    def __str__(self):
        '''
        Cada vez que invoquemos un objeto de tipo Question nos dará la siguiente información
        '''
        return self.question_text

    #definiendo método personalizado
    def was_published_recently(self):
        '''
        Este método va a devolver verdadero o falso si la pregunta
        fue publicada recientemente.
        '''
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
        


#Segundo modelo Choice
class Choice(models.Model):
    #se define la llave foránea que hace que estos registros se conecten con Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    #Con default decimos que tendrá como primer valor el número cero
    votes = models.IntegerField(default=0) 

    def __str__(self):
        '''
        Cada vez que invoquemos un objeto de tipo Question nos dará la siguiente información
        '''
        return self.choice_text