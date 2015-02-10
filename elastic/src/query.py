__author__ = 'Geolffrey Mena <gmjun2000@gmail.com>'
from elasticsearch import Elasticsearch
from elastic.src.search import config_search
from elastic.src.config import *

es = Elasticsearch()

# MY_TYPE = "user"
MAX_TERMS_QUERY = 25
# TEXT_TO_FIND = "Francis"


def search(query, max_size=10):
    """
    Search fuzzy on elasticsearch
    query: the search param
    """
    # fields_to = fields_search[type_to_find]
    return es.search(
        index=JDBC_META_INDEX,
        doc_type=config_search['index'],
        size=max_size,
        body={
            "query": {
                "fuzzy_like_this": {
                    "fields": config_search['fields'],
                    "like_text": query,
                    "max_query_terms": MAX_TERMS_QUERY
                }
            }
        })


def search_by_type(type_as, query, max_size=10):
    config_search['index'] = [type_as]
    return search(query, max_size)


def cleaned_search(result):
    cleaned = []
    if result:
        for k, hit in result.items():
            if isinstance(hit, list):
                for r in hit:
                    new_result = {}
                    new_result['type'] = r.get('_type', None)
                    new_result['source'] = r.get('_source', None)
                    cleaned.append(new_result)
    return cleaned
