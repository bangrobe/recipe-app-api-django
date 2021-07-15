from django.urls import path, include

from user import views

app_name = 'user'
urlpatterns = [
    # name create co the duoc dung trong reverse url
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me')
]
