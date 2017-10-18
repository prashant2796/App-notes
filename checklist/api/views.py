from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	DjangoFilterBackend,
	)
from rest_framework import status
from .serializers import ChecklistSerializer,TaskSerializer
from notesapp.api.permissions import IsOwner
from checklist.models import Checklist
from rest_framework.response import Response
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)



class ChecklistViewSet(ModelViewSet):
	permission_classes = [IsAuthenticated,IsOwner]
	queryset=Checklist.objects.all()
	serializer_class = TaskSerializer

	filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]

	search_fields = ['title','tags','reminder_date','checklists__task_text','custom_tags__user_tag']
	ordering = ('-date_modified','-created_date')

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

	def perform_create(self,serializer):
		serializer.save(user=self.request.user)

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())   
		serializer = TaskSerializer(queryset, many=True, context={'request': request})
		return Response(serializer.data)

	def get_queryset(self):
		user = self.request.user.id
		queryset = Checklist.objects.filter(user=user)   
		return queryset

	def get_serializer(self, *args, **kwargs):
		if "data" in kwargs:
			data = kwargs["data"]
		    # check if many is required
			if isinstance(data, list):
				kwargs["many"] = True

		return super(ChecklistViewSet, self).get_serializer(*args, **kwargs)

	

	

	


	

	





        
       
        


        

        