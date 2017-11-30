# -*- coding: utf-8 -*-
from odoo import api, models, fields

class Sale_Order(models.Model):
	_inherit = "account.invoice"	
	
	RIF = fields.Integer(string='RIF', required = True, help = 'Ingresa rif del Cliente')
