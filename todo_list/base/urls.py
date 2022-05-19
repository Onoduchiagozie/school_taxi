
from django.urls import path
from . import views
from .views import   Booking_view, CustomLoginView, RecordsView,  SignUpView
from django.contrib.auth import views as auth_views


urlpatterns=[
        # CBV FOR LOGGING IN 
    path('',CustomLoginView.as_view(),name='login'),

    path('booking_page/',Booking_view.as_view(),name='booking'),

    #    BOOKING CONFIRMATION PAGE
    path('confirmation/', views.booking_confirmation,name='confirmation' ),

            # REGISTRATION CBV
    path("register", SignUpView.as_view(), name="register"),

    path("records", RecordsView.as_view(), name="records"),
    
    path('logout', auth_views.LogoutView.as_view(), name='logout'),


    
#     path('stuff', NewPostView.as_view(),name='stuff')
        # path('notify/', views.sendmessage,name='notify')




]
