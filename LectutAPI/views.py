from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from LectutAPI.models import *
from LectutAPI.serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from LectutAPI.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework import renderers

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('userlist', request=request, format=format),
		'courses': reverse('courselist', request=request, format=format)
	})


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer  

class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

class CommentList(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)	   	