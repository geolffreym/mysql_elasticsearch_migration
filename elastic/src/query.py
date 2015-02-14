__author__ = 'gmena'

from elasticsearch import Elasticsearch
from elastic.src.search import config_search
from elastic.src.config import *

es = Elasticsearch()

# MY_TYPE = "user"
MAX_TERMS_QUERY = 25
# TEXT_TO_FIND = "Francis"


def search(query, max_size=10, index=config_search['index']):
    """
    Busqueda en elastic
    @:param query Query search string
    @:param max_size max results
    @:param index Where?
    @:return dict
    """""
    # fields_to = fields_search[type_to_find]
    return es.search(
        index=JDBC_META_INDEX,
        doc_type=index,
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
    """
    Get a document with type match
    @:param type_as The type to find
    @:param query Query string
    @:param max_size Max results
    @:return dict
    """
    return search(query, max_size, [type_as])


def create_document(data, rtype):
    """
    Create a document
    @:param data dict
    @:param rtype string
    """
    return es.create(
        index=JDBC_META_INDEX,
        doc_type=rtype,
        body=data
    )


def delete_document(uid, rtype):
    """
    Delete a document
    :param uid int:
    :param rtype string:
    :return: dict
    """
    return es.delete_by_query(
        index=JDBC_META_INDEX,
        doc_type=rtype,
        body={
            "query": {
                "term": {
                    "id": uid
                }
            }
        }
    )


def cleaned_search(result):
    """
    Clean the search, with onle data needed
    :param result:
    :return dict:
    """
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
