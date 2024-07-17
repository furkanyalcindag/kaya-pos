{
    'name': 'customReport',
    'author': "Burcu Yurdakul",
    'category': '',
    'summary': 'Includes reporting in accordance with the regulation',
    'version': '1.0',
    'depends': ['base', 'purchase','stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/report_base_menu.xml',
        'report/purchase_operation_report.xml',
        'report/ir_actions_report.xml',
        'report/stock_picking_report.xml',
        'views/purchase_operation_report_views.xml',
        'views/stock_picking_report_views.xml',

    ],
    'images': ['static/description/icon.png'],
    'application': True,
    'installable': True,
}
