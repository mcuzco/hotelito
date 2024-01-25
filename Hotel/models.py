from django.db import models

# Create your models here.
class Room (models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    price = models.IntegerField(verbose_name="Precio")
    image = models.ImageField(verbose_name="Imagen", upload_to= "rooms")
    NumPeople = models.IntegerField(verbose_name="Numero de Personas")
    NumRoom = models.IntegerField(verbose_name="Numero de Habitaciones")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'
        ordering = ["-created"]
    def __str__(self):
        return self.title 
    
class Reservation(models.Model):
    date = models.DateField(verbose_name="Fecha de Reservacion")
    cliente = models.CharField(verbose_name="Cliente", max_length=100)
    mail = models.EmailField(verbose_name="Email")
    room = models.CharField(max_length=100,verbose_name="Habitacion")
    user = models.CharField(max_length=100,verbose_name="Usuario")
    class Meta:
        verbose_name = 'Reservacion'
        verbose_name_plural = 'Reservaciones'
        ordering = ["-date"]
    def __str__(self):
        return self.cliente

class About (models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to= "about")
    image_security = models.ImageField(verbose_name="Imagen de Seguridad", upload_to= "about")
    description_security = models.TextField(verbose_name="Descripcion de Seguridad")
    image_price = models.ImageField(verbose_name="Imagen de Precio", upload_to= "about")
    description_price = models.TextField(verbose_name="Descripcion de Precio")
    image_availability = models.ImageField(verbose_name="Imagen de Disponibilidad", upload_to= "about")
    description_availability = models.TextField(verbose_name="Descripcion de Disponibilidad")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Nosotro'
        verbose_name_plural = 'Nosotros'
        ordering = ["-created"]
    def __str__(self):
        return self.title 

class Blog (models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    date = models.DateField(verbose_name="Fecha")
    author = models.CharField(max_length=100, verbose_name="Autor")
    image = models.ImageField(verbose_name="Imagen", upload_to="blog")
    description = models.TextField(verbose_name="Descripcion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
        ordering = ["-created"]
    def __str__(self):
        return self.title 

class Testimony(models.Model):
    description = models.TextField(verbose_name="Descripcion")
    author = models.CharField(max_length=200, verbose_name="Autor")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimoniales'
        ordering = ["-created"]
    def __str__(self):
        return self.author
    
class Asesoria (models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    mail = models.CharField(max_length=200, verbose_name="E-mail")
    cell = models.CharField(max_length=100, verbose_name="Telefono")
    msg = models.TextField(verbose_name="Mensaje")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Asesoria'
        verbose_name_plural = 'Asesorias'
        ordering = ["-created"]
    def __str__(self):
        return self.name