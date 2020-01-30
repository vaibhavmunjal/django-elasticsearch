from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

from .models import Search

def search_view(request):
	if request.method == 'GET':
		matched_search = Search.objects.all()

		q = request.GET.get('q')
		description = request.GET.get('description')

		if q:
			matched_search = matched_search.filter(name=q)

		if description:
			matched_search = matched_search.filter(description__icontains=description)

		return render(request, 'search/search.html', context={'matched_search':matched_search})

	return HttpResponse('<h3>Only Get method Is Allowed</h3>')