from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,url
from . import views

urlpatterns=[
    url(r'api/user/user-id/(?P<pk>[0-9]+)/$',
        views.UserDescription.as_view()),
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$',
        views.ProjectDescription.as_view()),
    url(r'^home/',views.home,name='home'),
    url('^$',views.profile,name ='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^user/',views.user,name ='user'),
    url(r'^rate/',views.rate,name ='rate'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^api/profile/', views.UserList.as_view()),
    url(r'^api/project/', views.ProjectList.as_view()),
    url(r'^article/',views.new_article,name ='newsarticle'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)