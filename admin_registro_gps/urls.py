from django.conf import settings
from django.conf.urls import url

#from admin_registro_gps.views import index

from admin_registro_gps.views import *
from . import views


urlpatterns = [
    
    url(r'^administrativo/', index),
    url(r'^$', index), # PAGINA RAIZ
    ##url(r'^$', views.index, name='index'), TAMBEM FUNCIONAL SE IMPORTAR from . import views

]

