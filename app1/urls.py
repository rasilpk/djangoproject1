
from django.urls import path
from.import views
urlpatterns =[
    path("",views.home),
    path("about",views.about),
    path("contact/",views.contact,name="contact"),
    path("viewbook/",views.viewbook,name="viewbook"),
    path("addbook/",views.addbook,name='addbook'),
    path("update/<int:id>",views.update_book,name='updatebook'),
    path("delete/<int:id>",views.delete_book,name='deletebook')
]