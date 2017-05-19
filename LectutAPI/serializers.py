from rest_framework import serializers
from LectutAPI.models import *
from django.contrib.auth.models import User


class CourseSerializer(serializers.ModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
	class Meta:
		model = Course
		fields = ('courseName','posts', 'id', 'users' )

class PostSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	course = serializers.ReadOnlyField(source='course.courseName')
	comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
	class Meta:
		model = Post
		fields = ('post','pub_time', 'course', 'owner', 'id' )	

class CommentSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	post = serializers.ReadOnlyField(source='post.post')

	class Meta:
		model = Comment
		fields = ('comment','pub_time', 'post', 'owner', 'id'  )		

class UserSerializer(serializers.ModelSerializer):
	courses = CourseSerializer(many=True, read_only=True)
	posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
	comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
	class Meta:
		model = User
		fields = ('id', 'username', 'courses', 'posts', 'comments') 