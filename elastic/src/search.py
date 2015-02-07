__author__ = 'Geolffrey Mena <gmjun2000@gmail.com>'

"""
Here the fields to use are declared in Search
fields: ["param_sql1", "param_sql2"].
index: ["the index declared in meta.py user, client, etc.."]

These fields are associated with the db queries therefore be
be relevant
"""
config_search = {
    "fields": ("identification", "name" ),
    "index": ("user", "client")
}