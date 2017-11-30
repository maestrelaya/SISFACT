# -*- coding: utf-8 -*-
{
	'name': 'SISFACT',
    'version': '1.0',
    'depends': ['base_setup', 'sale'],
    'authors': 'Sandra Maestre y José Agelvis',
    'category': 'Creación de Facturas',
    'description': """
    Facturar
    """,
    'update_xml': [],
    "data" : [
		"views/sisfact_clientes_view.xml" , 
		"views/sale_views.xml"
        ],
    'installable': True,
    'auto_install': False,
}
