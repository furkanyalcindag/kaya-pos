from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    isyeri = fields.Char(string='Isyeri')
    username = fields.Char(string='Username')
    password = fields.Char(string='Password')
    catalog = fields.Char(string='Catalog')
    status = fields.Selection([('draft', 'Draft')])

    birfatura_canli_test = fields.Selection([
        ('0', 'Canli'),
        ('1', 'Test'),
    ], 'Live or test integration', config_parameter='birfatura_canli_test', default='0')




