# -*- coding: utf-8 -*-
{
    'name': "modulo bebida cafe",

    'summary': "Un modulo que mide el nivel de cansancio de los alumnos y se le recomienda que tomar",

    'description': """
Modulo que simula un pequeño programa que mide el nivel de sueño de los estudiantes y segun este se le recomienda
una bebida con cafeina.
    """,

    'author': "CabbaGG Corp.",
    'website': "https://www.CabbaGG.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

