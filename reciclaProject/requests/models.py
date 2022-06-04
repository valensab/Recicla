from django.db import models
from users.models import User
from publications.models import Publication

# Create your models here.
class Request(models.Model):
    id_request = models.AutoField(primary_key=True, unique = True)
    date = models.DateField('Fecha',auto_now_add=True, auto_now=False)
    recycler = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Solicitante')
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE,verbose_name = 'Publicación')
    state = models.CharField('Estado', max_length = 30, blank = True, null = True, default="Pendiente")
    comments = models.CharField('Comentarios', max_length = 254, blank = True, null = True)
    is_active = models.BooleanField('Activa',default=True)
 
    class Meta:
        ordering = ["-date",]
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'

    def __str__(self):
        return f'{self.date} {self.recycler}'