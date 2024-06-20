from django.db import models

# Create your models here.
class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length=200) #Cria uma entrada de texto de 200 linhas
    date_added = models.DateTimeField(auto_now_add=True) #Registrar data e hora automaticamente
    
    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text
    
class Entry(models.Model):
    """anotação especifica"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
        def __str__(self):
            """Devolve uma string do modelo"""
            return self.text[:50] + '...'