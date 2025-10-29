# -*- coding: utf-8 -*-
{
    'name': "Inheritance Demo",
    'summary': "Demonstrates _inherits and standard _inherit (extension)",
    'description': """
        A simple module to show different inheritance types:
        - Defines a base 'demo.human' model.
        - 'demo.customer' uses _inherits (delegation).
        - Extends 'demo.human' using _inherit (extension) to add Superhuman fields/methods.
    """,
    'author': "Baobao",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/human_views.xml',    # Load view Human (đã bao gồm Superhuman)
        'views/customer_views.xml', # Load view Customer
        'views/superhuman_views.xml',
        'views/menu_views.xml',     # Load menu
    ],
    'application': True,
}