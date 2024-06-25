from odoo import models, fields, api


class ProductInventoryCountLine(models.Model):
    _name = 'product.inventory.count.line'
    _description = 'Product Inventory Count Line'

    product_id = fields.Many2one('product.product', string='Products')
    inventory_count_id = fields.Many2one("product.inventory.count", string="Inventory Count")
    initial_quantity = fields.Float(string="Initial Quantity")
    counted_quantity = fields.Float(string="Counted Quantity")
    difference = fields.Float(string="Difference", compute='_compute_difference')  # auto calculation


    @api.depends('initial_quantity', 'counted_quantity')
    def _compute_difference(self):
        for line in self:
            line.difference = line.counted_quantity - line.initial_quantity

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            initial_quantity = self.product_id.qty_available
            self.initial_quantity = initial_quantity

    # @api.model
    # def update_product_field(self, location):
    #     if location:
    #         stock_quants = self.env['stock.quant'].search([
    #             ('location_id', '=', location.id),
    #             ('product_id', '!=', False)
    #         ])
    #         products = stock_quants.mapped('product_id')
    #         return {
    #
    #             'domain': {
    #                 'product_id': [('id', 'in', products.ids)]
    #             }
    #         }
    #

