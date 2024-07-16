{
    'name': 'product_inventory_count',
    'author': "Burcu Yurdakul",
    'category': 'Inventory',
    'summary': 'Module for tracking monthly product stock counts',
    'version': '1.0',
    'depends': ['base', 'product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/product_inventory_view.xml',
        'views/product_inventory_count_line_view.xml',
    ],
    'images': ['static/description/icon.png'],
    'application': True,
}
