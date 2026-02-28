{
    'name': 'Customer Credit Control',
    'version': '1.0',
    'category': 'Sales/Accounting',
    'summary': 'Manage customer credit limits and block sales if exceeded',
    'depends': ['sale', 'account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/credit_limit_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}