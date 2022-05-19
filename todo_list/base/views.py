from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.contrib.auth.views import LoginView
from base.models import Record
from .forms import SignUpForm
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# stripe.api_key='sk_test_51Kpv01ITTZjH3MU1ZgR33XD4coNkCuW7w8FIaZ7T5idVYEcnGLhJSEzWRcmVv7tY703qpHoCK45oEnBf7ZngWeFo0061chbEns'


class CustomLoginView(LoginView):
    template_name='base/login.html'


@method_decorator(login_required, name='dispatch')
class Booking_view(TemplateView):
    template_name='base/booking_page.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'base/register.html'

@login_required
def booking_confirmation(request):
    pick=request.GET['pick']
    drop=request.GET['drop']

    drop_coordinate=drop[10:]
    picks_coordinate=pick[10:]
    
    pickup_name=pick[:10]
    drop_name=drop[:10]
    name =request.user
    
    import requests
    import json  
    url= f'https://maps.distancematrixapi.com/maps/api/distancematrix/json?destinations={drop_coordinate}&origins={picks_coordinate}&key=AlphaDMAVFrZ4nGKXA0m2m6tUD4RQfEUqYhL7Kpw'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    values = response.text
    y = json.loads(values)
    distance = y['rows'][0]['elements'][0]['distance']['text']
    time = y['rows'][0]['elements'][0]['duration']['text']
    distance_int= distance[:4]
    price=round(float(distance_int) * 200)


    # DISTANCE FROM USER FROM CLIENT
    student=picks_coordinate
    driver='6.8722398,7.4016781'
    url= f'https://maps.distancematrixapi.com/maps/api/distancematrix/json?destinations={driver}&origins={student}&key=AlphaDMAVFrZ4nGKXA0m2m6tUD4RQfEUqYhL7Kpw'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    values = response.text
    y = json.loads(values)
    driver_time_to_student = y['rows'][0]['elements'][0]['duration']['text']




    all_records=Record(name=name,pickup_id=pickup_name,
                        drop_id=drop_name,price=price,
                        distance=distance)
    all_records.save()

    return render(request,'base/confirmation_page.html',
            {'time':time,'distance':distance,'price':price,
            'pickup_name':pickup_name,'drop_name':drop_name,'driver_time_away':driver_time_to_student})


@method_decorator(login_required, name='dispatch')
class RecordsView(ListView):
    template_name='base/records.html'
    def get_queryset(self):
        return Record.objects.filter(name=self.request.user)
   


  
