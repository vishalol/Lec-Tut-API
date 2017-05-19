from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^courseList/$', views.CourseList.as_view(), name = 'courselist'),
    url(r'^courseList/(?P<pk>[0-9]+)$', views.CourseDetail.as_view(), name = 'coursedetail'),
	url(r'^users/$', views.UserList.as_view(), name = 'userlist'),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name = 'userdetail'),
	url(r'^$', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)