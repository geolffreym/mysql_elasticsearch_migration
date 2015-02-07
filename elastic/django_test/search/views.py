from django.views.generic import TemplateView
from elastic.src.query import search, search_by_type, cleaned_search


class Search(TemplateView):
    template_name = 'layout/search/result.html'

    def post(self, request, **kwargs):
        search_query = request.POST.get('search_query', None)
        search_type = request.POST.get('search_type', None)
        hits = []

        if search_query is not None:
            if search_type is None:
                search_result = search(search_query)
            else:
                search_result = search_by_type(search_type, search_query)
            hits = search_result.get('hits')

        return self.render_to_response({'hits': cleaned_search(hits)})

# Create your views here.
