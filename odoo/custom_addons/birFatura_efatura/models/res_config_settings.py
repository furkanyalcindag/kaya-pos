from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    isyeri = fields.Char(string='Isyeri', required=True)
    username = fields.Char(string='Username', required=True)
    password = fields.Char(string='Password', required=True)
    catalog = fields.Char(string='Catalog', required=True)

    birfatura_canli_test = fields.Selection([
        ('0', 'Canli'),
        ('1', 'Test'),
    ], 'Live or test integration', config_parameter='birfatura_canli_test', default='0')