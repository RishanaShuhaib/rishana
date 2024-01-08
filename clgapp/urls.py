from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('ind', views.ind, name='ind'),
    path('coursepage', views.coursepage, name='coursepage'),
    path('add_course', views.add_course, name='add_course'),
    path('studentpage', views.studentpage, name='studentpage'),
    path('add_student', views.add_student, name='add_student'),
    path('showstd/', views.showstd, name='showstd'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('editpage/<int:pk>/', views.editpage, name='editpage'),
    path('deletestd/<int:pk>/', views.deletestd, name='deletestd'),
    path('signup', views.signup, name='signup'),
    path('login1', views.login1, name='login1'),
    path('usercreate', views.usercreate, name='usercreate'),
    path('userhome', views.userhome, name='userhome'),
    path('edituserpage', views.edituserpage, name='edituserpage'),
    path('edituser/<int:pk>/', views.edituser, name='edituser'),   
    path('display', views.display, name='display'),
    path('showstcr/', views.showtcr, name='showtcr'),
    path('deletetcr/<int:pk>/', views.deletetcr, name='deletetcr'),
    path('logout',views.logout,name='logout'),
    
    
]
    

    
