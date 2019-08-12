from src.utils import LuceneSearchException


class ElasticLuceneSearchFilterMixin:
    def lucene_filter_search(self, searchset_class, search_terms, search):
        if searchset_class is not None:
            try:
                return searchset_class.filter(search, search_terms)
            except LuceneSearchException:
                return None
        return None

    def filter_search(self, request, search, view):
        search_terms = self.get_base_search_terms(request)

        # if there nothing to search - return
        if not search_terms:
            return search

        searchset_class = self.get_searchset_class(view, request)
        filtered_search = self.lucene_filter_search(searchset_class=searchset_class, search_terms=search_terms,
                                                    search=search)

        if filtered_search is None:
            filtered_search = search.extra(size=0)

        return filtered_search
