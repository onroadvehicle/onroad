from django.urls import path, include
from vehicle import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
     path('home/',views.homeview.as_view()),
     path('contact/',views.contactview.as_view()),
     path('about_us/',views.about_usview),
     path('gallary/',views.gallaryview),
     path('blogs/',views.blogsview),
     path('blogdetail/<int:id>',views.blogdetailview),
     path('services/',views.servicesview.as_view()),
     path('faq/',views.faqview),
     path('login/',LoginView.as_view(),name="login"),
     path('logout/',LogoutView.as_view(),name="logout"),
     path('signup/',views.signupview),
     path('insertcontact/',views.insertcontact),
     path('insertappointment/',views.insertappointment),
     path('appointment/',views.appointmentview),
   
   
]