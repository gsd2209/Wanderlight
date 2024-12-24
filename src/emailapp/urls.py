from django.urls import path
from .views import *

<<<<<<< HEAD

urlpatterns = [
    path("/send", SendEmailView.as_view()),
]
=======
urlpatterns = [
    path('/send',SendEmailView.as_view()),
]
>>>>>>> 6472ae2acf6526a1fb1173eadcbb7c15ed4b071a
