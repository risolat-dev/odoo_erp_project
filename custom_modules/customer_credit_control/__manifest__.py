{
    'name': 'Customer Credit Control',
    'depends': ['base', 'sale'],  # SHU QATORNI TEKSHIRING
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/credit_limit_views.xml',
    ],
    'installable': True,
}