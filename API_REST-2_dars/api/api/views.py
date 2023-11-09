from api.api.serializers import EmployeeSerializer
from api.models import Employee
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def employee_list(request, format=None):
    if request.method == 'GET':
        employeis = Employee.objects.all()
        serializer = EmployeeSerializer(employeis, many=True)

        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('success', safe=False)
        return JsonResponse('errors', safe=False)


@api_view(['GET'])
def employee_detail(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employee)

    return JsonResponse(serializer.data, safe=False)
