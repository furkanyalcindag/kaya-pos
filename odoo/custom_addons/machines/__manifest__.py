{
    'name': 'Machines',
    'author': "Kaya",
    'category': 'Manufacturing/Manufacturing',
    'summary': 'Makine Yönetimi',
    'website': 'https://www.Kaya.com',
    'version': '17.0.0.1.0',
    'depends': ['base', 'hr'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/machines_view.xml'
    ],
     'installable': True,
    'application': True,
}