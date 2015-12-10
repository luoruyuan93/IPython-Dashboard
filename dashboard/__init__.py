# -*- coding: utf-8 -*-
from __future__ import absolute_import

# built-in package
import copy
import logging
import logging.config

# third-parth package
import redis
from flask import Flask
from flask.ext.restful import Api

# user-defined package
from .conf import config
from .server.utils import Map

'''
dashboard server setup
'''
# app = Flask("__name__", static_folder="./static", template_folder="./templates")
# app = Flask("dashboard", static_folder="./static", template_folder="./templates")
# app = Flask("dashboard")
app = Flask(__name__)
api = Api(app)


'''
dashboard common services setup
'''
r_kv = redis.Redis(host=config.redis_kv_host, port=config.redis_kv_port, db=config.redis_kv_db)
r_db = redis.Redis(host=config.redis_db_host, port=config.redis_db_port, db=config.redis_db_db)


'''
build sql connector
'''
# build_sql_connector()


'''
logging init
'''
log = Map()
logging.config.fileConfig('dashboard/conf/logging.conf')
access_log = logging.getLogger('access')
error_log = logging.getLogger('error')
log.access = access_log
log.error = error_log


# import modules
from . import client, server


'''
Details here
'''

def build_sql_connector():
    if config.db_type == 'mysql':
        import MySQLdb
        connector = MySQLdb.connect(host=config.sql_host, port=config.sql_port,
                                    db=config.sql_db, user=config.sql_user,
                                    password=config.sql_password)
        return connector
    else:
        pass
