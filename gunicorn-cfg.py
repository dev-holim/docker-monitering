# -*- encoding: utf-8 -*-
"""
gunicorn --config gunicorn-cfg.py run:app
gunicorn -k eventlet -w 1 run:app
"""

bind = '0.0.0.0:8000'
workers = 1
worker_class = 'eventlet'
accesslog = '-'
loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True
