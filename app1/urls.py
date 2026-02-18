
from django.urls import path
from.import views
urlpatterns =[
    path("",views.home),
    path("about",views.about),
    path("contact/",views.contact,name="contact"),
    path("viewbook/",views.viewbook,name="viewbook"),
    path("addbook/",views.addbook,name='addbook')
]