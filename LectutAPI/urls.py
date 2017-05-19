from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^courseList/$', views.CourseList.as_view(), name = 'courselist'),
    url(r'^courseList/(?P<pk>[0-9]+)$', views.CourseDetail.as_view(), name = 'coursedetail'),
	url(r'^users/$', views.UserList.as_view(), name = 'userlist'),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name = 'userdetail'),
	url(r'^$', views.api_root),
    url(r'^postList/$', views.PostList.as_view(), name = 'postlist'),
    url(r'^postList/(?P<pk>[0-9]+)$', views.PostDetail.as_view(), name = 'postdetail'),
    url(r'^commentList/$', views.CommentList.as_view(), name = 'commentlist'),
    url(r'^commentList/(?P<pk>[0-9]+)$', views.CommentDetail.as_view(), name = 'commentdetail'),    	
]

urlpatterns = format_suffix_patterns(urlpatterns)