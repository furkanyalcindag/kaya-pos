{
    'name': 'Inter Company Stock Transfer',
    'version': '17.0.1.0.0',
    'category': 'Inventory',
    'summary': """Create counterpart Receipt/Delivery Orders between
     companies.""",
    'description': """Automatically Create Receipt/Delivery orders if any
     company validates a Deliver Order/Receipt to the selected company,
     Inter Company Stock Transfer, Stock Transfer,Create counterpart
     Receipt/Delivery Orders between companies""",
    'author': 'Burcu YURDAKUL',
    'company': 'Comitfy Bilişim Teknolojileri',
    'maintainer': 'Comitfy Bilişim Teknolojileri',
    'website': "https://www.comitfy.com",
    'depends': ['stock', 'account'],
    'data': [
        'views/res_company_views.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
