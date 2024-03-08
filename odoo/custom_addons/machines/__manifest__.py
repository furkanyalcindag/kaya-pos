{
    'name': 'Machines',
    'author': "Kolaysis",
    'category': 'Manufacturing/Manufacturing',
    'summary': 'Makine Yönetimi',
    'website': 'https://www.kolaysis.com',
    'version': '17.0.0.1.0',
    'depends': ['base', 'hr', 'mrp'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/machines_view.xml'
    ],
     'installable': True,
    'application': True,
}