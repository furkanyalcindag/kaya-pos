{
    'name': 'Bir Fatura Efatura Entegrasyonu',
    'author': "Kerem Can Turgut",
    'category': '',
    'summary': 'BirFatura Entegrasyonu',
    'version': '17.0.0.1.0',
    'depends': ['base', 'account'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/birfatura_view.xml',
        'views/res_config_settings_view.xml'
    ],
     'installable': True,
    'application': True,
}