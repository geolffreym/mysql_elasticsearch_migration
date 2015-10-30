ELASTICSEARCH SIMPLE MIGRATION
===============================
This is a simple example of migration from mysql to elasticsearch using JDBC in python

To start just run
 ```
python run/migrate_all.py
```

DEPENDENCIES
------------

elasticsearch-python (>= 1.4.0) 

[Go to Elastic Python Home](http://www.elasticsearch.org/guide/en/elasticsearch/client/python-api/current/)

elasticsearch ( >= 1.4.2 - <= 1.4.4) 

[Go to Install ElasticSearch](http://www.elasticsearch.org/guide/en/elasticsearch/guide/current/_installing_elasticsearch.html)


jdbc-river

Just copy the "odbc" into the directory "elasticsearch plugins" folder ex: (/usr/share/elasticsearch/plugin)

[JDBC](https://github.com/jprante/elasticsearch-jdbc)



CONTRIBUTE
---------
Create your own search methods in query.py
[Go to Elastic Python DOC](http://elasticsearch-py.readthedocs.org/en/latest/api.html)


PLAYING TRICKS
--------------
http://www.elasticsearch.org/blog/playing-http-tricks-nginx/

ABOUT
======

######config.py
Contains the basic configuration of the module, you can set your constant and configure your connections

######meta.py
Contains all sql queries associated with each entity type to search

######search.py
Contains the configuration fields and indexes to associate to search

######query.py
It is the most important files because it contains the methods used to search

######migration.py
Contains the methods to use for migration from mysql to elastic
