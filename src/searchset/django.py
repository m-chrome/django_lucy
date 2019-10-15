from django.core.exceptions import FieldError
from django.db.models import ForeignKey

from .base import BaseSearchSet
from ..searchset.fields.django import DjangoSearchField, DjangoSearchFieldWithoutWildcard
from ..searchset.mapping import DjangoMapping
from ..parser import LuceneToDjangoParserMixin


class DjangoSearchSet(LuceneToDjangoParserMixin, BaseSearchSet):
    _field_base_class = DjangoSearchFieldWithoutWildcard
    _default_field = DjangoSearchField
    _field_type_to_field_class = dict()

    @classmethod
    def filter(cls, queryset, search_terms):
        query = cls.parse(raw_expression=search_terms)
        try:
            return queryset.filter(query)
        except FieldError:
            return queryset.none()

    # for search helper

    _mapping_class = DjangoMapping

    @classmethod
    def _get_raw_mapping(cls):
        return [field.name for field in cls.Meta.model._meta.fields if not isinstance(field, ForeignKey)]
