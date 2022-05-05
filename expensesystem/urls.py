from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard', views.index,name="dashboard"),
    path('loginpage', views.loginPage, name="loginpage"),
    path('registerpage', views.register, name="registerpage"),
    path('logoutpage', views.logoutUser, name="logoutpage"),
    path('list_expense',views.list_expense, name="list_expense") ,
    path('list_category',views.list_category, name="list_category") ,
    path('add_category',views.add_category, name="add_category") ,
    path('add_expense',views.add_expense, name="add_expense") ,
    path('delete_expense/<expense_id>/',views.delete_expense, name="delete_expense") ,
    path('update_expense/<expense_id>/',views.update_expense, name="update_expense") ,
    path('update_category/<category_id>/',views.update_category, name="update_category"),
    path('monthly_expense', views.monthly_expense, name="monthly_expense"),
    path('export_pdf', views.export_pdf, name="export_pdf"),
    path('sort/<name>/', views.sort, name="sort"),
    path('reset_password/', auth_views.PasswordResetView.as_view() , name='reset_password') ,
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view() , name="password_reset_done") ,
    # email link 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view() , name="password_reset_confirm") ,
    #change password
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view() ,name="password_reset_complete") ,
    path('list_income',views.list_income, name="list_income") ,
    path('add_income',views.add_income, name="add_income") ,
    path('account/', views.accountSettings, name="account"),
    path('update_income/<income_id>/',views.update_income, name="update_income"),
    path('delete_income/<income_id>/',views.delete_income, name="delete_income") ,


]