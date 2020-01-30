from django.urls import path

from .views import search_view, elastic_search_view

urlpatterns = [
	path('', search_view, name='search'),
	path('elastic', elastic_search_view, name='elastic_search')
]