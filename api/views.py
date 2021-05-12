from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Region
from .serializers import RegionsSerializer


class RegionList(APIView):
	def get(self, request):
		regions = Region.objects.all()
		serializer = RegionsSerializer(regions, many=True)
		return Response(serializer.data)

	def post(self):
		pass