# -*- coding: utf-8 -*-
{
    'name': "pdca",

    'summary': """
        PDCA MODULE
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Allal",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'pdca',
    'version': '0.1',
    'installable': True,
    # any module necessary for this one to work correctly
    'depends': ['base','mail','contacts'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/unite_view.xml',
        'views/direction_view.xml',
        'views/processus_view.xml',
        'views/constat_view.xml',
        'views/affectation_pilote_view.xml',
        'views/action_view.xml',
        'views/templates.xml',
        'data/mail_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
