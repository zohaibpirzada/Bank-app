from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index, name='index'),
    path("transfer/", views.money_transfer, name='transfer'),
    path("login/", views.user_login, name='login'),
    path("logout/", views.user_logout, name='logout'),
    path("sign_up/", views.Sign_up, name='sign'),
    path("transfer/conform/<str:sender>-to-<str:reciver>-<int:send_amount>", views.conform, name='conform'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

