# -*- coding: utf-8 -*-

{
    'name': 'Transfer Payment Acquirer',
    'category': 'Hidden',
    'summary': 'Payment Acquirer: Transfer Implementation',
    'version': '1.0',
    'description': """Transfer Payment Acquirer""",
    'author': 'OpenERP SA',
    'depends': ['payment_acquirer'],
    'data': [
        'views/transfer.xml',
        'data/transfer.xml',
    ],
    'installable': True,
}
