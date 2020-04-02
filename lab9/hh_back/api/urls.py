from django.urls import path
from .views import companies_list,company_detail,company_vacancies,vacancy_list,vacancy_detail,top10
urlpatterns = [
    path('companies/',companies_list),
    path('companies/<int:company_id>',company_detail),
    path('companies/<int:company_id>/vacancies',company_vacancies),
    path('vacancies/',vacancy_list),
    path('vacancies/<int:vacancy_id>/',vacancy_detail),
    path('vacancies/top_ten',top10),
    ]