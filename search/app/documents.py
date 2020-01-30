from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Search

@registry.register_document
class SearchDocument(Document):
    class Index:
        name = 'search_result'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Search

        fields = [
            'id',
            'name',
            'description',
        ]
