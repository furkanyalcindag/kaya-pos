import json
import logging
from datetime import date

from odoo import models, fields
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class StockPickingReport(models.Model):
    _name = 'stock.picking.report'
    _description = 'Stock Picking Report'
    # _auto = False

    company_id = fields.Many2one('res.company', string='Şirket')
    invoice_date = fields.Date(string='Fatura Tarihi')
    report_data = fields.Text()
    current_date = fields.Date()

    def stock_picking_report(self):
        company_id = self.env.context.get('company_id')
        if not company_id:
            raise UserError("Şirket ID'si bulunamadı.")

        domain = [('company_id', '=', company_id), ('picking_type_id.code', '=', 'incoming')]
        pickings = self.env['stock.picking'].search(domain)
        products = []
        for picking in pickings:
            for move in picking.move_line_ids:

                purchase_line = move.move_id.purchase_line_id

                invoices = []
                if purchase_line:
                    invoices = purchase_line.order_id.invoice_ids

                for invoice in invoices:
                    invoice_date="---"
                    if invoice.invoice_date:
                        invoice_date = invoice.invoice_date.strftime("%d/%m/%Y")
                    invoice_number = invoice.name
                    product = move.product_id
                    category = product.categ_id.name
                    quantity = move.quantity
                    uom = product.uom_id.name
                    purchase_price = purchase_line.price_unit
                    purchase_total = purchase_price * quantity
                    sale_price = product.lst_price
                    sale_total = sale_price * quantity

                    products.append({
                        'name': picking.name,
                        'product': product.name,
                        'type': category,
                        'qty': quantity,
                        'uom': uom,
                        'purchase_price': purchase_price,
                        'purchase_total': purchase_total,
                        'sale_price': sale_price,
                        'sale_total': sale_total,
                        'invoice_date': invoice_date,
                        'invoice_number': invoice_number,


                    })
        report_data=[]
        if products:
            report_data.append({
                'products': products

                # Gerekli diğer alanları ekleyin
            })

            report = self.env['stock.picking.report'].search([('company_id', '=', company_id)], limit=1)
            _logger.info("Report Data: %s", report_data)

            if report:
                report.write({
                    'report_data': json.dumps(report_data),
                    'current_date': date.today()
                })
            else:
                report = self.env['stock.picking.report'].create({
                    'report_data': json.dumps(report_data),
                    'current_date': date.today()
                })

            return self.env.ref('customReport.action_report_stock_picking').report_action(report)
        else:
            raise UserError("İç Dağıtım Bilgisi Bulunamadı.")
