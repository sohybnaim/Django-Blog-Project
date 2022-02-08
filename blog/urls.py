from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
     #rest_framework URLs.
    path('api-all', views.api_all_users, name='api-all'),
    path('api-one/<user_id>', views.api_one_user, name='api-one'),
    path('api-add', views.api_add_user, name='api-add'),
    path('api-edit/<user_id>', views.api_edit_user, name='api-edit'),
    path('api-del/<user_id>', views.api_del_user, name='api-del')
 ]