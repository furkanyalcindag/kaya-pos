import logging

from odoo import models, fields, api


class Machines(models.Model):
    _name = 'machines'

    ip_address = fields.Char(required=True)
    name = fields.Char(required=True, default='Default Machine')
    place = fields.Char(required=True)
    port = fields.Char(required=True, digits=(5, 2))
    serial_no = fields.Char(required=True)

    @api.depends('port')
    def _compute_example_method(self):
        # 'mrp_workorder' modelinden belirli bir alanı içeren verileri çekmek için sorgu
        workorder_records = self.env['mrp.workorder'].search([])
        for workorder in workorder_records:
            print('workorder name = ', workorder.name)
            print('workorder production id = ', workorder.production_id.id)
            print('workorder workcenter id(iş emri) = ', workorder.workcenter_id.id)
        machine_records = self.env['machines'].search([])
        for machine in machine_records:
            print('machine name = ', machine.name)

    example_field = fields.Char(
        compute='_compute_example_method',
        string="Example Field",
        store=True  # Bu, değerin saklanmasını sağlar, böylece daha sonra okunabilir
    )

    # Burada aynı portta isimler atayamayız.
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
