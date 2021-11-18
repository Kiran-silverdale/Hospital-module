# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalBill(models.Model):
    _name = "hospital.bill"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Bills"

    bill_id = fields.Char(string='Reference', required=True, copy=False, index=True, default=lambda self: _('New'))
    date = fields.Date(string='Date')
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment ID", tracking=True)
    patient_id = fields.Char(string='Patient Name', tracking=True, related="appointment_id.patient_id.name", readonly=True)
    doctor_charges = fields.Integer(string='Doctor Charges', tracking=True, related="appointment_id.doctor_id.charges", readonly=True)
    room_charges = fields.Integer(string='Room Charges', tracking=True, related="appointment_id.room_id.room_charges", readonly=True)
    Lab_charges = fields.Integer(string='Lab Charges', tracking=True, related="appointment_id.lab_test_id.Amount", default=0, readonly=True)
    No_of_days = fields.Integer(string='No. of Days')
    total = fields.Integer(string='Total', compute='_compute_total')


    def _compute_total(self):
        for rec in self:
            s_total = rec.doctor_charges + (rec.room_charges * rec.No_of_days) + rec.Lab_charges
            rec.total = s_total

    @api.model
    def create(self, vals):
        if vals.get('bill_id', _('New')) == _('New'):
            vals['bill_id'] = self.env['ir.sequence'].next_by_code('hospital.bill') or _('New')
        return super(HospitalBill, self).create(vals)

    def name_get(self):
        result = []
        for rec in self:
            name = '[' + rec.bill_id + '] ' + rec.patient_id
            result.append((rec.id, name))
        return result