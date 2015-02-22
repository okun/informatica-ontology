# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 12:43:17 2015

@author: toporkov
"""

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
from app import views