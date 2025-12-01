# -*- coding: utf-8 -*-
{
    'name': "leed_malditos",

    'summary': "Módulo para contar el numero de veces que un profesor manda leer a los alumnos",

    'description': """
Mucho texto, modulo que dice que leemos poco entonces hay que leer mas, este modulo permite llevar un conteo
de cada ocasión que un profesor remite el alumno a la documentación.
    """,

    'author': "Daniel Castelao",
    'website': "https://www.danielcastelao.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv', #Esta linea es la que se tiene que descomentar
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

