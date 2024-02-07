from odoo import models, fields


class Versions(models.Model):
    _name = 'versions'

    version = fields.Char(required=True)
    description = fields.Char(required=True)