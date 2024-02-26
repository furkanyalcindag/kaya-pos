import zeep

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    isyeri = fields.Char(string='Isyeri', default="SUBECOMITFY")
    username = fields.Char(string='Username', default="USERCOMITFY")
    password = fields.Char(string='Password', default="USERCOMITFY")
    catalog = fields.Char(string='Catalog', default="EFATURATEST")
    trnstartdate = fields.Date()
    trnenddate = fields.Date()

    birfatura_canli_test = fields.Selection([
        ('Canli', 'Canli'),
        ('Test', 'Test'),
    ], 'Live or test integration', config_parameter='birfatura_canli_test', default='Canli')

    status = fields.Selection([
        ('Aktif', 'Aktif'),
        ('Pasif', 'Pasif'),
    ], 'Live or test integration', config_parameter='status', default='Pasif')

    gbpk = fields.Selection([
        ('GB', 'Gönderilen Fatura'),
        ('PK', 'Gelen Fatura'),
    ], 'Live or test integration', config_parameter='gbpk', default='GB')

    dateisinv = fields.Selection([
        ('true', 'Evet'),
        ('false', 'Hayır'),
    ], 'Live or test integration', config_parameter='isinv', default='true')

    @api.model_create_multi
    def create(self, vals):
        wsdl = 'https://outapi-test.einvoiceplatform.com/efatura.svc?wsdl'
        client = zeep.Client(wsdl=wsdl)
        res = super(ResConfigSettings, self).create(vals)
        print(f"Oluşturulan isyeri adı: {res.isyeri}")
        print(f"Oluşturulan username adı: {res.username}")
        print(f"Oluşturulan password adı: {res.password}")
        print(f"Oluşturulan catalog adı: {res.catalog}")
        print(f"Oluşturulan birfatura_canli_test: {res.birfatura_canli_test}")
        trnenddate = res.trnenddate.strftime('%d.%m.%Y')
        trnstartdate = res.trnstartdate.strftime('%d.%m.%Y')
        print(f"Oluşturulan trnenddate: {trnenddate}")
        print(f"Oluşturulan trnstartdate: {trnstartdate}")

        clientUser = {
            'Catolog': res.catalog,
            'İsyeri': res.isyeri,
            'Password': res.password,
            'Username': res.username
        }

        sonuc = client.service.GetInvoiceList(clientUser, res.gbpk, trnstartdate, trnenddate, res.dateisinv)



        print(f"sonuc: {sonuc.text}")

        return res
