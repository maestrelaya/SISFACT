# -*- coding: utf-8 -*-
{
	'name': 'SISFACTV2',
    'version': '2.0',
    'depends': ['base_setup','account' , 'account_accountant'],
    'authors': 'Sandra Maestre y José Agelvis',
    'category': 'Creación de Facturas',
    'description': """
    Facturar
    """,
    'update_xml': [],
    "data" : [ 
		#"views/sisfact_clientes_view.xml" ,
        "views/sale_order_view.xml" ,
        "views/res_partner_view.xml"
        ],
    'installable': True,
    'auto_install': False,
}
