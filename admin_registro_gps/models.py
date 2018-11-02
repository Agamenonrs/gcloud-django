# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import *

#connect(DBNAME)

class Monitor(Document):

	linha = StringField(max_length=10, required=True)
	data_inicio = StringField(required=True)
	data_limite = StringField(required=True)

	'''
	def __init__(self,linha,data_inicio,data_limite):
		self.linha = linha
		self.data_inicio = str(data_inicio)
		self.data_limite = str(data_limite)
		
	def toJSON(self):
        	return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
	'''
	

class Monitor2(models.Model):
   	linha = models.CharField(max_length=10, null=False)
