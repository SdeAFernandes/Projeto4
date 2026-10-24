from django.contrib import admin          
from django.urls import path, include    
from rest_framework.routers import DefaultRouter  
from filmes.views import FilmesViewSet, GenerosViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'generos', GenerosViewSet)  # registra endpoints para generos
router.register(r'filmes', FilmesViewSet)   # registra endpoints para filmes


urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include(router.urls)),
   path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
    