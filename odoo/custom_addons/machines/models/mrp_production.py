from odoo import models, fields


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    machines_id = fields.Many2many('machines')

    def action_confirm(self):
        res = super(MrpProduction, self).action_confirm()
        print("Selamın Alikim")
        return res
