# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class herencia_sale_order(models.Model): 
    _inherit = "sale.order" 
    
    
    id_RIF = fields.Many2one("res.partner", string = "RIF")
    
 
    
 
