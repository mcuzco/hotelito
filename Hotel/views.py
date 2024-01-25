from datetime import datetime, timedelta
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView, View
from.models import About,Room,Blog,Testimony,Reservation,Asesoria
from django.contrib.auth import logout, authenticate, login as auth_login
from.forms import SignUpForm, SignipForm
from django.http import HttpResponse
import stripe
stripe.api_key = 'sk_test_51LaU1pIOntAHsdbGjPGqs9szKakV8jdmc0AWwJ8uiomlBilW8EJgmlXVk1KrB6NkROsYUXJBncGEsVD8Yd0lfzen008cJCLM4z'
# Create your views here.

def login(request):
    if request.method=="POST":
        form=SignipForm(request,data=request.POST)
        if form.is_valid():
            nombre=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            user=authenticate(request,username=nombre, password=contra)
            if user is not None:
                auth_login(request,user)
                return redirect('home')
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.success(request, "Informacion incorrecta")
    form = SignipForm
    return render(request, 'hotel/Login.html',{'form':form})

class registrar(TemplateView):
    template_name = 'hotel/Registrar.html'
    def get(selt, request):
        form = SignUpForm
        return render(request, selt.template_name,{'form':form})
    def post(selt, request):
        form= SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, selt.template_name, {'form':form})
        
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

class home(TemplateView):
    template_name = 'hotel/index.html'
    def get(selt, request):
        about = About.objects.all()
        rooms = Room.objects.all()
        blog = Blog.objects.all()
        testimony = Testimony.objects.all()
        return render(request, selt.template_name, {'rooms': rooms, 'about': about, 'blog': blog, 'testimony': testimony})

class nosotros(TemplateView):
    template_name = 'hotel/Nosotros.html'
    def get(selt, request):
        about = About.objects.all()
        return render(request, selt.template_name, {'about': about})

class blog(TemplateView):
    template_name = 'hotel/Blog.html'
    def get(selt, request):
        blog = Blog.objects.all()
        return render(request, selt.template_name, {'blog': blog})

class blogentrada(TemplateView):
    template_name = 'hotel/Blog-entrada.html'
    def get(selt, request, titulo):
        blog = Blog.objects.filter(title = titulo)
        return render(request, selt.template_name, {'blog': blog})

class anuncios(TemplateView):
    template_name = 'hotel/Anuncios.html'
    def get(selt, request):
        room = Room.objects.all()
        return render(request, selt.template_name, {'room': room})

class anuncio(TemplateView):
    template_name = 'hotel/Anuncio.html'
    def get(selt, request, titulo):
        fec = datetime.today()+timedelta(days=1)
        fecha = fec.strftime('%Y-%m-%d')
        room = Room.objects.filter(title = titulo)
        return render(request, selt.template_name,{'room':room, 'fecha':fecha})
    
def cargo(request, titulo):
    room = Room.objects.filter(title=titulo)
    fec = datetime.today()+timedelta(days=1)
    fecha = fec.strftime('%Y-%m-%d')
    if request.method=="POST":
        date = request.POST["date"]
        reser = Reservation.objects.filter(room=titulo, date=date)
        if reser.exists():
            messages.warning(request, "Fecha de reservacion no disponible")
            return render(request, 'hotel/Anuncio.html',{'room':room, 'fecha':fecha })
        else: 
            price = request.POST["price"]
            user =request.POST["user"]
            client=request.POST["client"]
            email=request.POST["email"]
            token = request.POST['stripeToken']
            usd = int(price) * 100
            try:
                customer = stripe.Customer.create(
                email = email,
                name = client,
                source = token
                )   
                charge = stripe.Charge.create(
                customer = customer,
                amount = usd,
                currency = 'usd',
                description = titulo
                )
                reservacion = Reservation()
                reservacion.date=date
                reservacion.user= user
                reservacion.cliente=client
                reservacion.mail=email
                reservacion.room= titulo
                reservacion.save()
                messages.success(request, "Reservacion exitosa")
                pass
            except stripe.error.CardError as e:
                messages.warning(request,e.user_message)
            
        return render(request, 'hotel/Anuncio.html',{'room':room, 'fecha':fecha})   
    else:
        return render(request, 'hotel/Anuncio.html',{'room':room, 'fecha':fecha })

class reservacion(TemplateView):
    template_name = 'hotel/Reservaciones.html'
    def get(selt, request):
        reser = Reservation.objects.all()
        return render(request, selt.template_name, {'reser': reser})
    
class misreservacion(TemplateView):
    template_name = 'hotel/MisReservaciones.html'
    def get(selt, request):
        reser = Reservation.objects.all()
        return render(request, selt.template_name, {'reser': reser})
    
class Reservaspdf(View):
    def get(selt, request, *args, **kwargs):
        reser = Reservation.objects.all()
        template = get_template('hotel/Mis.html')
        data ={
            'reser' : reser
        }
        html = template.render(data)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)
        return response
    def post(selt, request,):
        return redirect('reservacion')
    
class contacto(TemplateView):
    template_name = 'hotel/contacto.html'
    def get(selt, request):
        return render(request, selt.template_name)
    def post(selt, request):
        if request.method=="POST":
            mail = request.POST["email"]
            asess = Asesoria.objects.filter(mail=mail)
            if asess.exists():
                messages.warning(request, "Ya tiene una asesoria en curso")
                return redirect('contacto')
            else: 
                name=request.POST["nombre"]
                tel=request.POST["telefono"]
                msg=request.POST["mensaje"]
                asesoria = Asesoria()
                asesoria.name= name
                asesoria.mail= mail
                asesoria.cell= tel
                asesoria.msg= msg
                asesoria.save()
                messages.success(request, "Formulario enviado exitosamente")
                return redirect('contacto')
        else:
            return redirect('contacto')
        
class asesoria(TemplateView):
    template_name = 'hotel/Asesoria.html'
    def get(selt, request, id):
        ass = Asesoria.objects.filter(id = id)
        if ass.exists():
            ass.delete()
            messages.success(request, "La asesoria se registro como realizada")
        ases = Asesoria.objects.all()
        return render(request, selt.template_name, {'ases': ases})

    