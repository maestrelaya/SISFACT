# -*- coding: utf-8 -*-
from odoo import api, models, fields


class sisfact_clientes(models.Model):
	_name = 'sisfact.clientes'
	
	
	CI_RIF =fields.Integer(string='Cédula / RIF: ', required = True, help = 'Ingresa la cedula o rif del Cliente')
	cliente=fields.Char(string ='Cliente: ', required = True, help = 'Ingresa el nombre del Cliente')
	direccion=fields.Text(string='Dirección: ',required = True, help = 'Ingresa la Direccion del Cliente')
	telefono=fields.Char(string='Teléfonos: ', required = True, help = 'Ingresa el telefono del Cliente')
	correo=fields.Char(string='Correo: ',required = True, help = 'Ingresa el correo del Cliente')
	active=fields.Boolean(string='Activo: ',required = True, help = 'Cliente Activo o Inactivo')	
	

	
