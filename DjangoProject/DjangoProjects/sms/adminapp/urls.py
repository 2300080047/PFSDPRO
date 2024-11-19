from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.projecthomepage, name='projecthomepage'),
    path('printpagecall/', views.printpagecall, name='printpagecall'),
    path('printpagelogic/', views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall,name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic,name='exceptionpagelogic'),
    path('randompagecall/',views.randompagecall,name='randompagecall'),
    path('randompagelogic/',views.randompagelogic,name='randompagelogic'),
    path('calculatorcall/',views.calculatorlogic,name='calculatorcall'),
    path('calculatorlogic/',views.calculatorlogic,name='calculatorlogic'),
    path('add_path/', views.add_task,name='add_task'),
    path('<int:pk>/delete/', views.delete_task,name='delete_task'),

    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('log_out/',views.log_out,name='log_out'),

    path('get_time_details/', views.get_time_details, name='get_time_details'),
    path('calculate_future_date/', views.calculate_future_date, name='calculate_future_date'),
    path('calculate_future_page/', views.calculate_future_page, name='calculate_future_page'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('upload_file/', views.upload_file, name='upload_file'),






    ]
