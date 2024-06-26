from odoo import models, fields, api
from odoo.http import request


class ProductInventoryCount(models.Model):

    _name = 'product.inventory.count'
    _description = 'Product Inventory Count'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.today())
    lines = fields.One2many('product.inventory.count.line', 'inventory_count_id', string='Inventory Lines')
    stock_location_id = fields.Many2one('stock.location', string='Stock Location')

    def view_inventory_lines(self):
        # lines alanına erişerek verileri döndür
        return {
            'name': 'Sayım Bilgileri',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'product.inventory.count.line',
            'domain': [('inventory_count_id', '=', self.id)],
            'context': {'search_default_inventory_count_id': self.id},
        }
    @api.model
    def create(self, vals):
        # Create the inventory count record
        inventory_count = super(ProductInventoryCount, self).create(vals)

        # Fetch all products in the selected stock location
        stock_quants = self.env['stock.quant'].search([
                     ('location_id', '=', inventory_count['stock_location_id'].id)
                ])

        # Create inventory count lines for each product
        inventory_count_lines = []
        for product in stock_quants:

            inventory_count_lines.append((0, 0, {
                'product_id': product.product_id.id,
                'initial_quantity':product.quantity,
                'inventory_count_id': inventory_count.id,
                # Add other fields if needed
            }))

        # Update the inventory count with the lines
        inventory_count.write({'lines': inventory_count_lines})
        request.redirect('/web#id=%s&view_type=form&model=product.inventory.count' % inventory_count.id)

        return inventory_count

    # @api.onchange('stock_location_id')
    # def update_lines(self):
    #     # location_id değiştiğinde çalışacak metod
    #     for line in self.lines:
    #         # productInventoryLine'daki update_additional_field metodunu çağır
    #         line.update_product_field(self.stock_location_id)

    # @api.onchange('stock_location_id')
    # def _onchange_products_in_location(self):
    #     stock_quants = self.env['stock.quant'].search([
    #         ('location_id', '=', self.stock_location_id.id)
    #     ])
    #     for quant in stock_quants:
    #         product = quant.product_id
    #         quantity = quant.quantity
    #         print(f"Product: {product.name}, Quantity: {quantity}")
