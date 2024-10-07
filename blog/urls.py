from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, CategoryViewSet, TagViewSet, UserViewSet
from rest_framework.authtoken import views 
from rest_framework.authtoken.views import obtain_auth_token



# Setting up the router
router = DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='post')  
router.register(r'categories', CategoryViewSet, basename='category')   
router.register(r'tags', TagViewSet, basename='tag')   
router.register(r'users', UserViewSet, basename='user')  

# Defining the urlpatterns
urlpatterns = [
    path('', include(router.urls)),  
    path('api-token-auth/', views.obtain_auth_token),
    path('api/login/', obtain_auth_token, name='api_token_auth'),

]
