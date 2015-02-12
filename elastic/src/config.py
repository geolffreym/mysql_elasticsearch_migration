__author__ = 'Geolffrey Mena <gmjun2000@gmail.com>'

"""
Please read documentation jdbc plugin elasticsearch
https://github.com/jprante/elasticsearch-river-jdbc
"""


# set mysql database http root
URL_DEFAULT = "jdbc:mysql://localhost:3306/mydb"

#mysql user
USER_DEFAULT = ""

#mysql password
PASSWORD_DEFAULT = ""

#default dont change
JDBC_TYPE = "jdbc"

#default dont change
JDBC_INDEX = "_river"

#the main index
JDBC_META_INDEX = "api"

#the doc type
JDBC_DOC_TYPE = "my_type"

#default dont change
JDBC_ID = "_meta"

META_DEFAULT = {
    "type": JDBC_TYPE,
    "jdbc": []
}

META_JDBC_DEFAULT = {
    "url": URL_DEFAULT,
    "user": USER_DEFAULT,
    "password": PASSWORD_DEFAULT,
    "index": JDBC_META_INDEX,
}
