{
    'name': 'Sale Approval Custom',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Approval workflow for sales orders exceeding $10,000',
    'depends': ['sale', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/approval_request_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}