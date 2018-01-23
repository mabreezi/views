from django.conf.urls import url
from first_app import views

urlpatterns = [
   url(r'^',views.index,name='index'),
   url(r'^$',views.asset, name='asset'),
   url(r'^$',views.transaction, name='transaction'),
   url(r'^$',views.trade, name='trade'),
]
