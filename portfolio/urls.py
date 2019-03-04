from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('results',views.results),
    # path('get_portfolio',views.get_portfolio),
    path('collect_user_data',views.collect_user_data),
    # path('style', views.styles),
]
