from rest_framework import serializers
from LectutAPI.models import *
from django.contrib.auth.models import User


class CourseSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
	user = serializers.HyperlinkedRelatedField(many=True, view_name='userdetail', read_only=True)
	class Meta:
		model = Course
		fields = ('courseName','posts', 'id', 'user' )

class PostSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	comments = serializers.HyperlinkedRelatedField(many=True, view_name='commentdetail', read_only=True)
	class Meta:
		model = Post
		fields = ('post','pub_time', 'course', 'owner', 'id','comments' )	

class CommentSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Comment
		fields = ('comment','pub_time', 'post', 'owner', 'id'  )		

class UserSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
	courses = serializers.HyperlinkedRelatedField(many=True, view_name='coursedetail', read_only=True)
	posts = serializers.HyperlinkedRelatedField(many=True, view_name='postdetail', read_only=True)
	comments = serializers.HyperlinkedRelatedField(many=True, view_name='commentdetail', read_only=True)
	class Meta:
		model = User
		fields = ('id', 'username', 'courses', 'posts', 'comments') 