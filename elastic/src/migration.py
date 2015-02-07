__author__ = 'gmena'
from elasticsearch import Elasticsearch
from elastic.src.config import *
from elastic.src.meta import *

es = Elasticsearch()

es.indices.delete(index=JDBC_INDEX, ignore=[400, 404])
es.indices.delete(index=JDBC_META_INDEX, ignore=404)


def migrate(types):
    meta_generated[types].update(META_JDBC_DEFAULT)
    meta_generated[types]['type'] = types
    META_DEFAULT['jdbc'].append(meta_generated[types])


def migrate_all():
    for k, meta in meta_generated.items():
        migrate(k)


def save_index():
    es.index(
        index=JDBC_INDEX,
        doc_type=JDBC_DOC_TYPE,
        id=JDBC_ID,
        body=META_DEFAULT
    )


print "Migration Complete"