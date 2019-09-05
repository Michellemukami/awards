from rest_framework import serializers
from .models import Profile,Project

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'post', 'pub_date','project_image')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'gender', 'bio','profile_image','user_id')