__author__ = 'Geolffrey Mena <gmjun2000@gmail.com>'
"""Just run to migrate all"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from elastic.src.migration import migrate_all, save_index

migrate_all()
save_index()