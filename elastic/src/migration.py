__author__ = 'gmena'
from elasticsearch import Elasticsearch
from elastic.src.config import *
from elastic.src.meta import *

es = Elasticsearch()

es.indices.delete(index=JDBC_INDEX, ignore=[400, 404])
es.indices.delete(index=JDBC_META_INDEX, ignore=404)


def migrate(types):
    """"
    Migrate by type
    @:param types
    """

    meta_generated[types].update(META_JDBC_DEFAULT)
    meta_generated[types]['type'] = types
    META_DEFAULT['jdbc'].append(meta_generated[types])


def migrate_all():
    """Migrate All"""
    for k, meta in meta_generated.items():
        migrate(k)


def save_index():
    """Save the index generated"""
    es.index(
        index=JDBC_INDEX,
        doc_type=JDBC_DOC_TYPE,
        id=JDBC_ID,
        body=META_DEFAULT
    )


print "Migration Complete"