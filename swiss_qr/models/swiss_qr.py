from odoo import fields, models, api, tools, _
from odoo.exceptions import ValidationError

class SwizzQR(models.Model):
    _name = 'swizz.qr'
    
    
    customer = fields.Char(string="Customer Id")
    ref_number = fields.Char(string="Ref Number")