from django.urls import path
from .views import industry_list, add_industry, industry_detail

urlpatterns = [
    path('industries/', industry_list, name='industry_list'),
    path('industries/add/', add_industry, name='add_industry'),
    path('industries/<int:industry_id>/', industry_detail, name='industry_detail'),
]
