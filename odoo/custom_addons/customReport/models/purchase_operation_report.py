import datetime
import json
from datetime import date

from odoo import api, models, fields
import logging

_logger = logging.getLogger(__name__)


class PurchaseOperationReport(models.Model):
    _name = 'purchase.operation.report'

    company_id = fields.Many2one('res.company', string='Şirket')
    report_data = fields.Text()
    current_date=fields.Date()


    @api.model
    def action_download_report(self, *args, **kwargs):
        company_id = self.env.context.get('company_id')
        if not company_id:
            raise ValueError("Şirket ID'si bulunamadı.")

        domain = [('company_id', '=', company_id)]
        purchases = self.env['purchase.order'].search(domain)

        report_data = []
        for purchase in purchases:
            products = []
            order_lines = purchase.order_line
            for line in order_lines:
                products.append({
                    'name': line.product_id.name,
                    'type':line.product_id.categ_id.name,
                    'uom':line.product_id.uom_id.name,
                    'unit_price':line.price_unit,
                    'price_subtotal': line.price_subtotal,

                })

            report_data.append({
                'name': purchase.name,
                'date_order': purchase.date_order.strftime('%Y-%m-%d'),
                'partner':  purchase.partner_id.contact_address,
                'amount_total': purchase.amount_total,
                'partner_ref': purchase.partner_ref,
                'products':products

                # Gerekli diğer alanları ekleyin
            })

        report = self.env['purchase.operation.report'].search([('company_id', '=', company_id)], limit=1)
        _logger.info("Report Data: %s", report_data)

        if report:
            report.write({
                'report_data': json.dumps(report_data),
                'current_date':date.today()
            })
        else:
            report = self.env['purchase.operation.report'].create({
                'report_data': json.dumps(report_data),
            })

        return self.env.ref('customReport.report_purchase').report_action(report)
