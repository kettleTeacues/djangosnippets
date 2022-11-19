from django.urls import path, include
from rest_framework import routers

from snippets import views, api_views as snippet_api_views

router = routers.DefaultRouter()
router.register('', snippet_api_views.SnippetViewSet)

urlpatterns = [
    path('new/', views.snippet_new, name='snippet_new'),
    path('<int:snippet_id>/', views.snippet_detail, name='snippet_detail'),
    path('<int:snippet_id>/edit/', views.snippet_edit, name='snippet_edit'),
    path('api/', include(router.urls)),
]
