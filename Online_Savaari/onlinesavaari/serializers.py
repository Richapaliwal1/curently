from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

# User Serializer
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password')

class AgentSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Agent
		fields = ('mobile', 'company_name', 'company_address', 'pincode', 'gstin', 'image', 'gst_state', 'country')
	def create(self, validated_data):
		user = Agent.objects.create_user(validated_data['username'], validated_data['email'], validated_data['mobile'], validated_data['company_name'], validated_data['company_address'], validated_data['pincode'], validated_data['gstin'], validated_data['gst_state'], validated_data['image'], validated_data['country'])
		return user
	

	
# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
	detail = AgentSerializer()
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password','detail',)
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
		return user

