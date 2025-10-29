{
    'name': 'My Bookstore',
    'version': '1.0',
    'summary': 'Module đơn giản để quản lý sách và test API Odoo',
    'author': 'Baao',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/bookstore_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'my_bookstore/static/src/css/style.css',
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
}