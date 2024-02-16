from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rota.models import *
from .serializer import *
from django.contrib.auth.models import User 
from rest_framework.viewsets import ModelViewSet
from rest_framework import status


class RotaUserViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'patch', 'delete',)
    queryset = RotaUser.objects.all()
    serializer_class = RotaUserSerialzer

class UserViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'patch', 'delete',)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['GET'])
    def custom_get_action(self, request, pk=None):
        # Custom action logic for GET request
        user = User.objects.get(pk=pk)
        user.first_name=request['username']
        # Retrieve data or perform any operation based on the instance with 'pk'
        return Response({'message': f'Custom GET action executed for instance {pk}.'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT,data="Item deleted")
    
class CaseViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'patch', 'delete',)
    queryset = Cases.objects.all()
    serializer_class = CasesSerializer

    @action(detail=False, methods=['POST'])
    def add_case(self, request, pk=None):
        # Custom action logic for request
        req = request.data
        assignee_name = User.objects.get(pk=req['assignee'])
        assignee = RotaUser.objects.get(user=req['assignee'])

        if(Cases.objects.filter(case_number=req['case_number']).values().exists()):
            get_case = Cases.objects.get(case_number=req['case_number'])
            get_case.assignee = assignee
            get_case.case_status = 'FTS'
            print("FTS DAPAT LOGIC")
            get_case.save()

        else:
            create_case = Cases(assignee=assignee, case_number=req['case_number'])
            create_case.save()
        
        return Response({'message': f'Case updated for {assignee_name.first_name}'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT,data="Case deleted")
