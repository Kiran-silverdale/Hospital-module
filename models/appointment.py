# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalAppointments(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Apointment"

    patient_id = fields.Many2one('hospital.patient', string="Patient Name", required=True, tracking=True)
    appointment_date = fields.Date(string="Appointment Date")

    doctor_id = fields.Many2one('hospital.doctor', string="Doctor Name", tracking=True)
    room_id = fields.Many2one('hospital.room', string="Room No.", tracking=True)
    lab_test_id = fields.Many2one('hospital.lab.record', string="Lab test", domain="[('patient_id', '=', patient_id)]")
    #doctor_ids = fields.Many2many('hospital.doctor', string="Doctors")
    age = fields.Integer(string='Age', tracking=True, related="patient_id.age", readonly=True)
    gender = fields.Selection(string='Gender', tracking=True, related="patient_id.gender", readonly=True)
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    #     ('other', 'other'),
    # ], required=True, default='male',tracking=True)
    # address = fields.Text(string='Address',tracking=True)

    disease = fields.Char(string='Disease', tracking=True, related="patient_id.disease", readonly=True)
    # disease = fields.Text(string='Disease',tracking=True)
    note = fields.Text(string='Description',tracking=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirm'),
                              ('done', 'Done'),
                              ('cancel', 'Cancel')],
                             default='draft',
                             string="Status",tracking=True)
    # doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    #
    name = fields.Char(string='Reference', required=True, copy=False, index=True, default=lambda self: _('New'))

    appointment_lines = fields.One2many('hospital.appointment.lines', 'appointment_id', string='Appointment Lines')
    pharmacy_note = fields.Text(string="Note", tracking=True)

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

    def action_draft(self):
        self.state = 'draft'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        return super(HospitalAppointments, self).create(vals)

    class HospitalAppointmentLines(models.Model):
        _name = 'hospital.appointment.lines'
        _description = 'Appointment Lines'

        product_id = fields.Many2one('product.product', string='Medicine')
        product_qty = fields.Integer(string="Quantity")
        appointment_id = fields.Many2one('hospital.appointment', string='Appointment ID')
        display_type = fields.Selection([
            ('line_section', "Section"),
            ('line_note', "Note")], default=False, help="Technical field for UX purpose.")