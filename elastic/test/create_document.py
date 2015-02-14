__author__ = 'gmena'
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from elastic.src.query import create_document


print create_document({"id": 1,
                       "first_name": "Frank",
                       "last_name": "Castellon"}, 'user')
