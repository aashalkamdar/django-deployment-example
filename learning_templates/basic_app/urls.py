from django.conf.urls import url
from basic_app import views
from django.urls import include,re_path

#template tagging
app_name = "basic_app"

urlpatterns = [
    re_path(r'^relative_url_templates/$',views.relative_url_templates,name='relative_url_templates'),
    re_path(r'^other/$',views.other,name='other'),
]
