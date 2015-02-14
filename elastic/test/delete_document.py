__author__ = 'gmena'
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from elastic.src.query import delete_document

print delete_document(1, 'users')
