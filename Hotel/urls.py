from django.urls import path
from .views import anuncio,anuncios,blogentrada,blog,home,nosotros,login, cargo
from .views import asesoria,registrar,cerrar_sesion,reservacion,misreservacion,Reservaspdf,contacto

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('login/', login, name="login"),
    path('cargo/<titulo>', cargo, name="cargo"),
    path('contacto/', contacto.as_view(), name="contacto"),
    path('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion"),
    path('registrar/', registrar.as_view(), name="registrar"),
    path('nosotros/', nosotros.as_view(), name="nosotros"),
    path('blog/', blog.as_view(), name="blog"), 
    path('blogentrada/<titulo>', blogentrada.as_view(), name="blogentrada"), 
    path('anuncios/', anuncios.as_view(), name="anuncios"), 
    path('anuncio/<titulo>', anuncio.as_view(), name="anuncio"), 
    path('reservacion/', reservacion.as_view(), name="reservacion"),
    path('misreservacion/', misreservacion.as_view(), name="misreservacion"),
    path('asesoria/<id>', asesoria.as_view(), name="asesoria"),
    path('misreservacionpdf/', Reservaspdf.as_view(), name="misreservacionpdf")
]
