from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('kicks/', views.kicks_index, name='index'),
    path('kicks/<int:kick_id>/', views.kicks_detail, name='detail'),
    path('kicks/create/', views.KickCreate.as_view(), name='kicks_create'),
    path('kicks/<int:pk>/update/', views.KickUpdate.as_view(), name='kicks_update'),
    path('kicks/<int:pk>/delete/', views.KickDelete.as_view(), name='kicks_delete'),
    path('kicks/int:<int:kick_id>/add_viewing', views.add_viewing, name='add_viewing'),
    path('kicks/<int:kick_id>/assoc_lace/<int:lace_id>/', views.assoc_lace, name='assoc_lace'),
    path('kicks/<int:kick_id>/disassoc_lace/<int:lace_id>/', views.disassoc_lace, name='disassoc_lace'),
    path('laces/', views.LaceList.as_view(), name='laces_index'),
    path('laces/<int:pk>/', views.LaceDetail.as_view(), name='laces_detail'),
    path('laces/create/', views.LaceCreate.as_view(), name='laces_create'),
    path('laces/<int:pk>/update/', views.LaceUpdate.as_view(), name='laces_update'),
    path('laces/<int:pk>/delete/', views.LaceDelete.as_view(), name='laces_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]