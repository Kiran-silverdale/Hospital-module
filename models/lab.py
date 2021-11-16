# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalLabs(models.Model):
    _name = "hospital.lab"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital labs"

    lab_no = fields.Char(string='Lab No.', required=True)
    date = fields.Date(string='Date')
    amount = fields.Text(string='Amount')
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    patient_id = fields.Many2one('hospital.patient', string="Patients")
    user_id = fields.Many2one('res.users', string="Responsible")
