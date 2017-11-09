# -*- coding: utf-8 -*-
from odoo import api, models, fields


class SaleOrder(models.Model):
	_inherit = 'sale.order'	
	
	CI_RIF =fields.Integer(string='Cédula / RIF', required = True, help = 'Ingresa la cedula o rif del Cliente')
	
	
