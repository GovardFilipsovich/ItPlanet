from django.urls import path
from RestApi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('accounts/', views.accounts_list),
    path('accounts/<int:pk>/', views.account_detail),
    path('registration/', views.reg),
]


urlpatterns = format_suffix_patterns(urlpatterns)
