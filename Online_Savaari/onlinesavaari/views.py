from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
# Create your views here.

def index(request):
	return render(request, "index.html", context={})

class UserDetailAPI(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (AllowAny,)
	
	def get(self,request,*args,**kwargs):
		user = User.objects.get(id=request.user.id)
		serializer = UserSerializer(user)
		return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


# Register API
class RegisterAPI(generics.GenericAPIView):
	serializer_class = RegisterSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		return Response({
		"user": UserSerializer(user, context=self.get_serializer_context()).data,
		"token": AuthToken.objects.create(user)[1]
		})

