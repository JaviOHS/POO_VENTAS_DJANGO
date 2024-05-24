from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.db.models.signals import post_migrate

@receiver(post_migrate)
def crear_grupos(sender, **kwargs):
    if kwargs.get('app_config').name == 'core':  # Asegúrate de que el código solo se ejecute cuando se migre la aplicación 'core'
        Group.objects.get_or_create(name='Administradores')
        Group.objects.get_or_create(name='Clientes')

@receiver(post_save, sender=User)
def asignar_permisos(sender, instance, created, **kwargs):
    if created:
        if instance.groups.filter(name='Administradores').exists():
            administradores = Group.objects.get(name='Administradores')
            permisos_administradores = Permission.objects.all()
            administradores.permissions.set(permisos_administradores)
        elif instance.groups.filter(name='Clientes').exists():
            # Aquí podrías asignar permisos específicos para clientes si lo necesitas
            pass