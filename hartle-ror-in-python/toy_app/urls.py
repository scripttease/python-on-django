from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    # path('', views.hello),
    path('', views.micropost_list, name='micropost_list'),
    path('users', views.user_list, name='user_list'),
    path('user/<int:pk>', views.user_show, name='user_show'),
    path('user/<int:pk>/edit', views.user_edit, name='user_edit'),
    path('user/new', views.user_new, name='user_new'),
    path('microposts', views.micropost_list, name='micropost_list'),
    path('micropost/<int:pk>', views.micropost_show, name='micropost_show'),
    path('micropost/<int:pk>/edit', views.micropost_edit, name='micropost_edit'),
    path('micropost/new', views.micropost_new, name='micropost_new'),
    url(r'^micropost/(?P<pk>\d+)/remove/$', views.micropost_remove, name='micropost_remove')
]

