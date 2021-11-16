# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalBill(models.Model):
    _name = "hospital.bill"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Bills"

    bill_id = fields.Char(string='Bill ID', required=True)
    date = fields.Date(string='Date')
    doc_charges = fields.Integer(string='Doctor Charges')
    room_charges = fields.Integer(string='Room Charges')
    No_of_days = fields.Integer(string='No. of Days')