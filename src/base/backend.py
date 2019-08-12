from rest_framework.filters import SearchFilter


class LuceneSearchFilter(SearchFilter):
    def get_searchset_class(self, view, request):
        """
        Returns searchset class if it presented in view
        """
        return getattr(view, 'search_class', None)

    def get_base_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        return request.query_params.get(self.search_param, '')
