from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from restapi.cakeshop.models import Cake
from restapi.cakeshop.serializers import CakeSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def cake_list(request):
    if request.method == 'GET':
        tutorials = Cake.objects.all()

        name = request.query_params.get('name', None)
        if name is not None:
            cakes = Cake.filter(name__icontains=name)

        cake_serializer = CakeSerializer(cakes, many=True)
        return JsonResponse(cake_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        cake_data = JSONParser().parse(request)
        cake_serializer = CakeSerializer(data=cake_data)
        if cake_serializer.is_valid():
            cake_serializer.save()
            return JsonResponse(cake_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(cake_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Cake.objects.all().delete()
        return JsonResponse({'message': '{} Cakes were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def cake_detail(request, pk):
    try:
        cake = Cake.objects.get(pk=pk)
    except Cake.DoesNotExist:
        return JsonResponse({'message': 'The Cake does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        cake_serializer = CakeSerializer(cake)
        return JsonResponse(cake_serializer.data)

    elif request.method == 'PUT':
        cake_data = JSONParser().parse(request)
        cake_serializer = CakeSerializer(cake, data=cake_data)
        if cake_serializer.is_valid():
            cake_serializer.save()
            return JsonResponse(cake_serializer.data)
        return JsonResponse(cake_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cake.delete()
        return JsonResponse({'message': 'Cake was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
