from django.shortcuts import render
from account.permissions import UserPermission
from .serializers import BornSerializer
from .models import BornModel
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# @api_view(['GET'])
class BornView(APIView):
    def endpoint(request):
        if request.method == 'GET':
             current_time = datetime.now()
             born = BornModel.objects.filter(time__gt=current_time, is_booked=False)
             serialized_born = BornSerializer(born, many=True)
             return Response(serialized_born.data)
