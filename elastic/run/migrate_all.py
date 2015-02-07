__author__ = 'Geolffrey Mena <gmjun2000@gmail.com>'
"""Just run to migrate all"""

from elastic.src.migration import migrate_all, save_index

migrate_all()
save_index()