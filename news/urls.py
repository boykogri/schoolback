from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers
from news.views import NewsViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'news', views.NewsViewSet)

news_list = NewsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
news_detail = NewsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', include(router.urls)),
    path('', news_list, name='news-list'),
    path('<int:pk>/', news_detail, name='news-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]