from odoo import models, api


class MrpProductionMachine(models.Model):
    _inherit = 'mrp.production'
    _name = 'mrp.machines'

    @api.model
    def action_confirm(self):
        result = super(MrpProductionMachine, self).action_confirm()

        if result:
            print("Selamın Alikim")
        else:
            print("action_confirm metodu çağrıldı ancak bir hata oluştu.")

        return result

