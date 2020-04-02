from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import JsonResponse, HttpResponse
from .models import Company, Vacancy
from django.db.models import Count

def companies_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)

def company_detail(request,company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'message does not exits'})
    return JsonResponse(company.to_json())


def company_vacancies(request,company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 404})

    vacancies = company.vacancy_set.all()
    vacancies_json = [p.to_json() for p in vacancies]
    return JsonResponse(vacancies_json,safe=False)


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json,safe=False)

def vacancy_detail(request,vacancy_id):
    try:
        vacancy=Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error':'message'})
    return JsonResponse(vacancy.to_json())

def top10(request):
    vacancies=Vacancy.objects.order_by('-salary')[:5]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json,safe=False)



