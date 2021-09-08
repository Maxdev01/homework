from django.urls import path

from . import views 


urlpatterns = [
    path('', views.indexpage, name='first'),
    path('atik-lekti/<int:id>',  views.li_atik, name="pageid"),
    path('inscription', views.authview, name='authentificate'),
    path('connexion', views.connecter, name='connexion'),

    path('mesipouvisitlan', views.dekonekte, name='logout'),

    path('articles', views.atikNouvo, name="detailpam"),
]