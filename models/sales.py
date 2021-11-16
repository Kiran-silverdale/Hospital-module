from odoo import fields, models

class saleOrder(models.Model):
    _inherit = "sale.order"

    sales_record = fields.Char(string="sales records")