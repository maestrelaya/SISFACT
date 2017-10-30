# -*- coding: utf-8 -*-
from openerp.osv from fields, osv

class clientes(osv.osv):
	_name = 'SISFACT.clientes'
	_rec_name = 'cliente'
	
	_columns = {
	'CI_RIF' : fields.integer('Cédula / RIF', size="10", required = True, help = 'Ingresa la cedula o rif del Cliente')
	'cliente' : fields.char('Cliente', size="80", required = True, help = 'Ingresa el nombre del Cliente')
	'direccion' : fields.date('Dirección',required = True, help = 'Ingresa la Direccion del Cliente')
	'telefono' : fields.char('Teléfonos', size="80", required = True, help = 'Ingresa el telefono del Cliente')
	'correo' : fields.char('Correo', size="80", required = True, help = 'Ingresa el correo del Cliente')
	'active' : fields.boolean('Activo',required = True, help = 'si esta activo la vista')
	
	}
