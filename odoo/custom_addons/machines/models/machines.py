from odoo import models, fields



class Machines(models.Model):
    _name = 'machines'

    ip_address = fields.Char(required=True)
    name = fields.Char(required=True, default='Default Machine')
    place = fields.Char(required=True)
    port = fields.Char(required=True, digits=(5, 2))
    serial_no = fields.Char(required=True)


    #Burada aynı portta isimler atayamayız.
    _sql_constraints = [
        ('unique_port', ' unique (port)', 'Bu port kullanılıyor lütfen tekrar port giriniz')
    ]

"""
    @api.constrains('ip_address')
    def _check_ip_address(self):
        for rec in self:
            if not rec.ip_address:
                raise ValidationError('Lütfen bir ip adres giriniz')
"""


