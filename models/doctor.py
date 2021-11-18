# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalDoctors(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    charges = fields.Integer(string='Charges', default=1000)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='male')
    address = fields.Text(string='Address')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    active = fields.Boolean(string="Active", default=True)
    doctor_id = fields.Char(string='Reference', required=True, copy=False, index=True, default=lambda self: _('New'))
    image = fields.Binary(string="Image")

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['hospital.appointment'].search_count([('doctor_id', '=', rec.id)])
            rec.appointment_count = appointment_count


    @api.model
    def create(self, vals):
        if vals.get('doctor_id', _('New')) == _('New'):
            vals['doctor_id'] = self.env['ir.sequence'].next_by_code('hospital.doctor') or _('New')
        return super(HospitalDoctors, self).create(vals)