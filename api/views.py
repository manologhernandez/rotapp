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

    #POST METHOD FOR CREATING USERS
    @action(detail=False, methods=['POST'])
    def add_user(self, request, pk=None):
        try:
            req = request.data
            create_user = User(
                username=req['username'],
                password=req['password'],
                first_name=req['first_name'],
                last_name=req['last_name'],
                is_active=req['is_active'],
            )
            #USER AUTOMATICALLY ADDDED ON ROTA USERS TABLE
            create_user.save()
            get_user = User.objects.get(username=req['username'])
            print(get_user)
            create_rota_user = RotaUser(
                user=get_user
            )
            create_rota_user.save()
            return Response({'message':'User Created'})
        
        except Exception as e:
            return Response({'error_message': f'Value Error Occurred on key: {e}'})  

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
        try:
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
                create_case = Cases(
                    assignee=assignee,
                    case_number=req['case_number']
                    )
                create_case.save()
            
            return Response({'message': f'Case updated for {assignee_name.first_name}'})
        
        except Exception as e:
            return Response({'error_message': f'Value Error Occurred on key: {e}'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT,data="Case deleted")
