from django.db import models
from users.models import User
from django.utils import timezone
# Create your models here.

class Publication(models.Model):
    id_publication = models.AutoField(primary_key=True, unique = True)
    type_material = models.CharField('Tipo de material', max_length = 254, blank = True, null = True)
    address = models.CharField('Dirección',max_length = 30, blank = True, null = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name = 'Usuario')
    weight = models.DecimalField('Peso', max_digits=10, decimal_places=3, blank = True, null = True)
    volume = models.DecimalField('Volumen', max_digits=10, decimal_places=3, blank = True, null = True)
    description = models.CharField('Descripción',  max_length = 254,blank = True, null = True)
    timestamp = models.DateTimeField('Fecha',auto_now_add=True, auto_now=False)
    state =  models.BooleanField('Estado', default = False)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return f'{self.id_publication} {self.type_material} {self.address} {self.user} {self.weight} {self.volume} {self.description} {self.timestamp} {self.state'