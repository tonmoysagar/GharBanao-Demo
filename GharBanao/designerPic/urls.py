from django.conf.urls import url
from .import views
urlpatterns = [
url(r'^$', views.HomeView.as_view(), name='home'),
url(r'^(?P<designerID>des[0-9]+)/$',views.des_profiles,name='des_profiles'),
url(r'^(add)/$',views.DesignersCreate.as_view(), name='register'),
url(r'^(?P<designerID>des[0-9]+)/update$',views.DesignersUpdate.as_view(),name='update'),
url(r'^(login)/$',views. UserFormView.as_view(), name='login'),
]