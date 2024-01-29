{
    'name': 'Machines',
    'author': "Kerem Can Turgut",
    'category': '',
    'summary': 'Makine Yönetimi',
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