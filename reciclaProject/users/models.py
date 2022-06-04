from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email,password, name,last_name, is_active, is_provider, is_recycler, is_staff, is_superuser, **extra_fields):
        user = self.model(
            email = email,
            name = name, 
            last_name = last_name,
            is_active = is_active,
            is_provider = is_provider,
            is_recycler = is_recycler,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email,name,last_name,password=None, **extra_fields):

        return self._create_user(email,password, name,last_name,False,False,False,False, False **extra_fields)

    def create_superuser(self,email, name, last_name, password=None, **extra_fields):
        return self._create_user( email, password, name, last_name,True,True,True, True, True,**extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Correo Electrónico',max_length = 254, unique = True,)
    name = models.CharField('Nombre', max_length = 50, blank = True, null = True)
    last_name = models.CharField('Apellido', max_length = 50, blank = True, null = True)
    phone_number = models.CharField("Número de telefono", max_length=10, null = True)
    address = models.CharField("Dirección", max_length=100, null = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_provider = models.BooleanField(default = False)
    is_recycler = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'
