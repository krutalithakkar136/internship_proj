from django.urls import path,include
from . import views
from .views import detail_view

urlpatterns=[
    path('',views.index,name='index'),
    path('services/',views.services,name="services"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('signup/',views.signup,name="signup"),
    path('shop/',views.shop,name="shop"),
    path('add_click/',views.add_click,name="add_click"),
    path('add_btn/',views.add_btn,name="add_btn"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('change_password/',views.change_password,name="change_password"),
    path('forgot_password/',views.forgot_password,name="forgot_password"),
    path('new_password/',views.new_password,name="new_password"),
    path('verify_otp/',views.verify_otp,name="verify_otp"),
    path('create_view/',views.create_view,name='create_view'),
    path('list_view/',views.list_view,name='list_view'),
    path('update_view/<id>',views.update_view,name='update_view'),
    path('delete_view/<int:id>',views.delete_view,name='delete_view'),
    path('contact/',views.contact,name="contact"),
    path('qr_gen/',views.qr_gen,name="qr_gen"),
    path('send/',views.qr_gen),
    path('accounts/', include('allauth.urls')),
    path('auth/google/', views.custom_login, name='custom_login'),
]


