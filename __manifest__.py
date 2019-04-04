# -*- coding: utf-8 -*-
{
    'name': "Maintenance 4.0",

    'summary': """
        Module de test pour implémentation Maintenance 4.0""",

    'description': """
        Module de test pour implémentation Maintenance 4.0
        Module de test pour implémentation Maintenance 4.0
        Module de test pour implémentation Maintenance 4.0
        Module de test pour implémentation Maintenance 4.0
        Module de test pour implémentation Maintenance 4.0
        Module de test pour implémentation Maintenance 4.0
        Module de test pour implémentation Maintenance 4.0
        Module de test pour implémentation Maintenance 4.0
        Module de test pour implémentation Maintenance 4.0
        Module de test pour implémentation Maintenance 4.0
        Module de test pour implémentation Maintenance 4.0
        Module de test pour implémentation Maintenance 4.0
    """,

    'author': "Tech-IT",
    'website': "http://www.tech-it.ma",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}