from odoo import models, fields


class Machines(models.Model):
    _name = 'machines'

    ip_address = fields.Char(required=True)
    name = fields.Char(required=True, default='Default Machine')
    place = fields.Char(required=True)
    port = fields.Char(required=True)
    serial_no = fields.Char(required=True)

    # Burada aynı portta isimler atayamayız.
    _sql_constraints = [
        ('unique_port', ' unique (port)', 'Bu port kullanılıyor lütfen tekrar port giriniz')
    ]

    # Bir makinayı sildiğimiz de neler yapabiliriz!
    """
    def unlink(self):
        res = super(Machines, self).unlink()
        print("Bir makina silindi")
        return res
    """
    # Bir makinayı düzenlediğimiz de neler yapabiliriz!
    """
    def write(self, vals):
        res = super(Machines, self).write(vals)
        print("Değiştirilen makina portu")
        return res
    """

    # Yeni bir makina oluştuğunda neler yapabiliriz!
    """"
    @api.model_create_multi
    def create(self, vals):
        res = super(Machines, self).create(vals)
        print(f"Oluşturulan makine adı: {res.name}")
        return res
    """


"""
    @api.constrains('ip_address')
    def _check_ip_address(self):
        for rec in self:
            if not rec.ip_address:
                raise ValidationError('Lütfen bir ip adres giriniz')
"""
